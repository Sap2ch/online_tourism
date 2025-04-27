from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.models import Profile

from django.urls import reverse_lazy
from articles.models import Article
from .forms import PostForm
from django.core.exceptions import PermissionDenied


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def logout_user(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('home'))

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get(self, request, slug):
        try:
            obj = Profile.objects.get(profile__username=self.kwargs['slug'])
        except Profile.DoesNotExist:
            raise render(self.request, './profile.html', context={'request': self.request, 'slug': self.kwargs['slug'].lower()})
        
        return render(request, './profile.html', context={'request': request, 'slug': self.kwargs['slug'].lower(), 'profile': obj})
    

class UsersView(ListView):
    """
        ВІДОБРАЖЕННЯ ЮЗЕРІВ
    """
    model = Profile
    template_name = 'users.html'
    context_object_name = 'profiles'
    # paginate_by = 


class MyPostsView(ListView):
    """
        ВІДОБРАЖЕННЯ ЮЗЕРІВ
    """
    model = Article
    template_name = 'my-posts.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(user=self.request.user)


class PostUpdateView(UpdateView):
    model = Article
    form_class = PostForm
    template_name = 'edit_post.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('article-url', kwargs={'slug': self.object.slug})

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.user != self.request.user:
            raise PermissionDenied("Ви не є автором статті!")
        
        return post
