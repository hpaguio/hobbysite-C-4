from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm
from user_management.models import Profile

@login_required
def commission_list(request):
    status_order = {
        'Open': 0,
        'Full': 1,
        'Completed': 2,
        'Discontinued': 3
    }
    commissions = Commission.objects.all().order_by(
        models.Case(
            *[models.When(status=status, then=models.Value(order)) for status, order in status_order.items()],
            default = models.Value(99),
            output_field = models.IntegerField()
        ),
        '-created_on'
    )
    
    for commission in commissions:
        jobs = commission.jobs.all()
        if not jobs.exists():
            continue

        all_full = True
        for job in jobs:
            accepted_count = JobApplication.objects.filter(job=job, status='Accepted').count()
            if accepted_count < job.manpower_required:
                all_full = False
                break
            
        if all_full and commission.status == "Open":
            commission.status = "Full"
            commission.save()
        elif not all_full and commission.status == "Full":
            commission.status = "Open"
            commission.save()
    
    created_commissions = Commission.objects.filter(created_by=request.user)

    applied_commissions = Commission.objects.filter(
        jobs__jobapplication__applicant = request.user.profile
    ).distinct()
    
    return render(request, 'commissions/commissions_list.html', {
        'commissions':commissions,
        'created_commissions':created_commissions,
        'applied_commissions':applied_commissions
    })

@login_required
def commission_details(request, param):
    commission = Commission.objects.get(id=param)
    jobs = Job.objects.filter(commission=commission)

    total_manpower = sum(job.manpower_required for job in jobs)

    job_info = []
    for job in jobs:
        accepted = JobApplication.objects.filter(job=job, status='Accepted').count()
        slots_open = max(0, job.manpower_required - accepted)
        user_applied = JobApplication.objects.filter(job=job, applicant__user=request.user).exists()
        
        can_apply = slots_open > 0 and not user_applied

        job_info.append({
            'job': job,
            'accepted': accepted,
            'slots_open': slots_open,
            'can_apply': can_apply,
            'user_applied': user_applied
        })
    
    total_slots_open = sum(info['slots_open'] for info in job_info)
    is_owner = commission.created_by == request.user
    creator_name = commission.created_by.profile.user

    return render(request, 'commissions/commissions_detail.html', {
        'commission': commission,
        'job_info': job_info,
        'total_manpower': total_manpower,
        'total_slots_open': total_slots_open,
        'is_owner': is_owner,
        'creator_name': creator_name,
    })