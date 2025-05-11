from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm
from user_management.models import Profile


class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.select_related('category', 'author').all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        context['previous_article'] = (
            Article.objects.filter(created_on__lt=article.created_on)
            .order_by('-created_on')
            .select_related('category')
            .first()
        )
        context['next_article'] = (
            Article.objects.filter(created_on__gt=article.created_on)
            .order_by('created_on')
            .select_related('category')
            .first()
        )

        # Comments
        context['comments'] = article.comments.select_related('author').order_by('created_on')
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles comment form submission directly on the Article detail page.
        """
        if not request.user.is_authenticated:
            return redirect("login")

        self.object = self.get_object()
        profile = get_object_or_404(Profile, user=request.user)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = profile
            comment.article = self.object
            comment.save()
            return redirect("wiki:article-detail", pk=self.object.pk)

        # Re-render with errors
        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki/article_form.html'
    fields = ['title', 'category', 'entry', 'image']

    def form_valid(self, form):
        form.instance.author = get_object_or_404(Profile, user=self.request.user)
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'wiki/article_form.html'
    fields = ['title', 'category', 'entry', 'image']

    def test_func(self):
        Article = self.get_object()
        return Article.author.user == self.request.user