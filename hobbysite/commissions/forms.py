from django import forms
from .models import Commission, Job, JobApplication
from user_management.models import Profile

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status', 'people_required']
        widgets = {
            'status': forms.Select(choices=Commission.status_choices),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []