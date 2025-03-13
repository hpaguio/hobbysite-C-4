from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'forum'

urlpatterns = [
    path('', PostListView.as_view(), name='forum-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='thread-detail'),
]