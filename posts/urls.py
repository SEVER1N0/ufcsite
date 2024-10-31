from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.lista_posts, name='index'),  # Listagem de posts
    path('<int:id>/', views.detalhe_post, name='detail'),  # Detalhes do post
]