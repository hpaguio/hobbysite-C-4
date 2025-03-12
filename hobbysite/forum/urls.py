from django.urls import path
from .views import PostListView, PostDetailView
from django.http import HttpResponseRedirect

app_name = 'forum'

urlpatterns = [
    path("", lambda request: HttpResponseRedirect("threads/")),  # Redirect base to threads
    path("threads/", PostListView.as_view(), name="thread-list"),
    path("thread/<int:pk>/", PostDetailView.as_view(), name="thread-detail"),
]
