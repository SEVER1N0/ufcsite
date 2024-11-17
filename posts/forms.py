from django import forms
from django.forms import ModelForm
from .models import Post, Comment, Category


class PostForm(ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
        label="Categorias"
    )

    class Meta:
        model = Post
        fields = [
            'titulo',
            'conteudo',
            'poster_url',
            'categories'
        ]
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'poster_url': 'URL do Poster',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }