from django.contrib import admin
from django.urls import path, include
from .views import Index, About, CreateArticleView, ArticleView, ArticlesByCategoryView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('create-article/', CreateArticleView.as_view(), name='create-article'),
    path('article/<slug:slug>/', ArticleView.as_view(), name='article-url'),
    path('category/<slug:slug>/', ArticlesByCategoryView.as_view(), name='articles_by_category'),
]
