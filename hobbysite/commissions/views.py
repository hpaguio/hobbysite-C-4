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

def commission_details(request, param):
    commissions = Commission.objects.get(id=param)
    comments = Comment.objects.filter(commission=commissions).order_by("-created_on")

    return render(request, 'commissions_detail.html', {'commission':commissions, 'comments':comments})