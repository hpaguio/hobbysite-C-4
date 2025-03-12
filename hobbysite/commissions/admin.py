from django.contrib import admin
from .models import Commission, Comment

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    
    list_display = ('title', 'created_on', 'updated_on')
    
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    
    list_display = ('commission', 'created_on', 'updated_on',)
    
admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
