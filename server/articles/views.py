from django.shortcuts import render
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from category import models

from .models import Article
from .forms import ArticleForm


class Index(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'articles'


class About(View):
    def get(self, request):
        return render(request, 'about.html', context={'request': request})
    

class CreateArticleView(LoginRequiredMixin, CreateView):
    template_name = 'create-article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user

        if not form.instance.slug:
            base_slug = slugify(form.instance.title)
            slug = base_slug
            n = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            form.instance.slug = slug

        return super().form_valid(form)

    
class ArticleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article-url.html'
    
class ArticlesByCategoryView(ListView):
    model = Article
    template_name = 'articles_by_category.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug']).order_by('-time_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = models.Category.objects.get(slug=self.kwargs['slug'])
        return context
