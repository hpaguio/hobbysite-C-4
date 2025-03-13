from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on')

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
