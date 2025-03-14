from django.urls import path
from .views import blog_categories, blog_article

urlpatterns = [
    path('blog/articles', blog_categories, name="blog_categories"),
    path('blog/article/<int:param>', blog_article, name="blog_article"),
    ]

app_name = "blog"