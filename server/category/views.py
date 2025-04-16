from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Category

class CategoryList(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'
