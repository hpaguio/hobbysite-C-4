from django.urls import path
from .views import blog_categories, blog_article

app_name = "blog"

urlpatterns = [
    path("", blog_categories, name="blog_home"),
    path("articles/", blog_categories, name="blog_categories"),
    path("article/<int:param>/", blog_article, name="blog_article"),
]