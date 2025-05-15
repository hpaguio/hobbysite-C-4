from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
)

app_name = "wiki"

urlpatterns = [
    path("", lambda request: HttpResponseRedirect(reverse_lazy("wiki:article-list"))),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("article/add/", ArticleCreateView.as_view(), name="article-create"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("article/<int:pk>/edit/", ArticleUpdateView.as_view(), name="article-edit"),
]