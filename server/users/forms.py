from django import forms
from articles.models import Article

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'category']
