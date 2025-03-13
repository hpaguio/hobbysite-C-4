from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'forum/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5  

    def get_queryset(self):
        return Post.objects.filter(category__isnull=False).select_related('category')

class PostDetailView(DetailView):
    model = Post
    template_name = "forum/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        context['previous_post'] = (
            Post.objects.filter(created_on__lt=post.created_on)
            .order_by('-created_on')
            .select_related('category')
            .first()
        )
        context['next_post'] = (
            Post.objects.filter(created_on__gt=post.created_on)
            .order_by('created_on')
            .select_related('category')
            .first()
        )
        return context