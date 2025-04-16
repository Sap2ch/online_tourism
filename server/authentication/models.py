from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    avatar = models.ImageField(upload_to='profile/%Y/%m/%d/', blank=True, verbose_name='Аватар')
    
    profile = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профіль'


    def __str__(self):
        return str(self.profile)
