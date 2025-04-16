from django.contrib import admin
from authentication.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile', 'avatar')

admin.site.register(Profile, ProfileAdmin)