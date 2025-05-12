from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Article, ArticleCategory, Comment
from .forms import CommentForm
from user_management.models import Profile

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_articles = Article.objects.select_related('category', 'author')
    
        if self.request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=self.request.user)
            user_articles = all_articles.filter(author=profile)
            other_articles = all_articles.exclude(author=profile)

            grouped_articles = {}
            for category in ArticleCategory.objects.all():
                grouped_articles[category] = other_articles.filter(category=category)

            context['user_articles'] = user_articles
            context['grouped_articles'] = grouped_articles
        else:
            grouped_articles = {}
            for category in ArticleCategory.objects.all():
                grouped_articles[category] = all_articles.filter(category=category)
            context['grouped_articles'] = grouped_articles

        return context
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/blog_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        context['other_articles_by_author'] = Article.objects.filter(
            author=article.author
        ).exclude(pk=article.pk)[:2]

        context['comments'] = article.comments.select_related('author').order_by('-created_on')
        context['comment_form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
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
            return redirect("blog:article-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'category', 'entry', 'image']

    def form_valid(self, form):
        form.instance.author = get_object_or_404(Profile, user=self.request.user)
        return super().form_valid(form)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'category', 'entry', 'image']
    raise_exception = True

    def test_func(self):
        article = self.get_object()
        return article.author.user == self.request.user