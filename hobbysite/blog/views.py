from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ArticleCategory, Article

# Create your views here.
def blog_categories(request):
    article_categories = ArticleCategory.objects.order_by("name")
    
    return render(request, 'article_list.html', {'article_category':article_categories})

def blog_article(request, param):
    article_categories = ArticleCategory.objects.get(id=param)
    articles = Article.objects.filter(category=article_categories).order_by("-created_on")
    
    return render(request, 'article.html', {'article_category': article_categories, 'article': articles})