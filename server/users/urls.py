from django.contrib import admin
from django.urls import path, include
from .views import ProfileView, logout_user, UsersView, PostUpdateView, MyPostsView

urlpatterns = [
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
    path('users/', UsersView.as_view(), name='users'),
    path('edit-post/<slug:slug>/', PostUpdateView.as_view(), name='update-post'),
    path('my-posts/', MyPostsView.as_view(), name='my-posts')
]
