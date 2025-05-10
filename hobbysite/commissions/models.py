from django.db import models
from django.contrib.auth.models import User
from user_management.models import Profile

class Commission(models.Model):
    status_choices = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=status_choices,
        default='Open'
    )
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commissions_created")
    updated_on = models.DateTimeField(auto_now=True)

class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name="jobs")
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(
        max_length=255,
        choices=[('Open','Open'),('Full','Full')],
        default='Open'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=255,
        choices=[('Pending','Pending'),('Accepted','Accepted'),('Rejected','Rejected')],
        default='Pending'
    )
    applied_on = models.DateTimeField(auto_now_add=True)
