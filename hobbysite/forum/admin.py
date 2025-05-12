from django.contrib import admin
from .models import ThreadCategory, Thread, Comment

@admin.register(ThreadCategory)
class ThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_on', 'updated_on')
    list_filter = ('category', 'created_on', 'updated_on')
    search_fields = ('title', 'entry', 'author__display_name')
    date_hierarchy = 'created_on'
    ordering = ('-created_on',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('entry_preview', 'author', 'thread', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('entry', 'author__display_name', 'thread__title')
    ordering = ('-created_on',)

    def entry_preview(self, obj):
        return obj.entry[:50] + ('...' if len(obj.entry) > 50 else '')
    entry_preview.short_description = 'Comment'