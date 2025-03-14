from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'forum'

urlpatterns = [
    path('', PostListView.as_view(), name='thread-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='thread-detail'),
]