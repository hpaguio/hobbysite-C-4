from django.urls import path
from .views import articles_list, articles_detail


urlpatterns = [
    path('articles/', articles_list, name="article_list"),
    path('article/<int:article_id>/', articles_detail, name="article_detail"),
]

app_name = "wiki"
