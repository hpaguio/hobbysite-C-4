from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Commission, Job, JobApplication
from user_management.models import Profile

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'created_on', 'updated_on', 'status', 'created_by')
    
class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ('role', 'commission', 'status', 'manpower_required', 'created_on')

class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    list_display = ('job', 'applicant', 'status', 'applied_on')
    
    def applicant(self, obj):
        return obj.applicant.display_name
    applicant.admin_order_field = 'applicant'
    applicant.short_description = 'Applicant'

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
    
admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
