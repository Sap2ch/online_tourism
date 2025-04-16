from django.contrib import admin
from django.urls import path, include
from .views import Index, About, CreateArticleView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('create-article/', CreateArticleView.as_view(), name='create-article'),
]
