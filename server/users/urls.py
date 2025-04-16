from django.contrib import admin
from django.urls import path, include
from .views import ProfileView, logout_user, UsersView

urlpatterns = [
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
    path('users/', UsersView.as_view(), name='users'),
]
