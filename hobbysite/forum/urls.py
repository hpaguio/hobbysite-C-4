from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'forum'  # This enables namespacing

urlpatterns = [
    path('', PostListView.as_view(), name='thread-list'),  # Keep this
    path('<int:pk>/', PostDetailView.as_view(), name='thread-detail'),  # Rename this
]