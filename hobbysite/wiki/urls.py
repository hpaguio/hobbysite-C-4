from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .views import (
    ThreadListView,
    ThreadDetailView,
    ThreadCreateView,
    ThreadUpdateView,
)

app_name = "forum"

urlpatterns = [
    path("", lambda request: HttpResponseRedirect(reverse_lazy("forum:thread-list"))),
    path("threads/", ThreadListView.as_view(), name="thread-list"),
    path("thread/add/", ThreadCreateView.as_view(), name="thread-create"),
    path("thread/<int:pk>/", ThreadDetailView.as_view(), name="thread-detail"),
    path("thread/<int:pk>/edit/", ThreadUpdateView.as_view(), name="thread-edit"),
]