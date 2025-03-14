from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    
    list_display = ('title', 'created_on', 'updated_on',)
    
class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    
    list_display = ('name', 'description',)
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)