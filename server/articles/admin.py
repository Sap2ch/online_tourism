from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'image', 'category', 'time_create', 'time_update', 'user')
    list_display_links = ('title', 'slug', 'user')

admin.site.register(Article, ArticleAdmin)
