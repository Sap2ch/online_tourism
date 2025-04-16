from django.db import models
from django.contrib.auth.models import User

from category.models import Category

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Опис')
    image = models.ImageField(upload_to='article/%Y/%m/%d/', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час оновлення')    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категорія')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    
    def __str__(self) -> str:
        return self.title
