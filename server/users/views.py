from typing import Any, Dict
from django.db import models
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from authentication.models import Profile

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
    model = Profile
    template_name = 'users.html'
    context_object_name = 'profiles'
    # paginate_by = 
