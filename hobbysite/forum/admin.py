from django.contrib import admin
from .models import PostCategory, Post

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on')
    list_filter = ('category', 'created_on')
    search_fields = ('title', 'entry')