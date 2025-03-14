from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Article, ArticleCategory

def articles_list(request):
    articles = Article.objects.order_by("-created_on")  # Sorted by latest first
    return render(request, 'wiki/articles_list.html', {'articles': articles})

def articles_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'wiki/articles_detail.html', {'article': article})