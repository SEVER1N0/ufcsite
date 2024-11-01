from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'conteudo',
            'poster_url',
        ]
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'poster_url': 'URL do Poster',
        }