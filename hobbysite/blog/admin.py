from django.contrib import admin
from .models import Article, ArticleCategory

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    
    list_display = ('title', 'created_on', 'updated_on',)
    
class CategoriesAdmin(admin.ModelAdmin):
    model = ArticleCategory
    
    list_display = ('title', 'description',)
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, CategoriesAdmin)