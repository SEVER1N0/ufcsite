from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()  
    data_postagem = models.DateTimeField(auto_now_add=True)  
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="posts", blank=True)

    def __str__(self):
        return self.titulo
    
class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    text = models.TextField() 
    created_date = models.DateTimeField(default=now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

