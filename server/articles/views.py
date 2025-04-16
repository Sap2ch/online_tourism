from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
        form.instance.user = self.request.user  # Присваиваем текущего пользователя
        return super().form_valid(form)