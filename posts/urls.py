from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.lista_posts, name='index'),
    path('search/', views.search_posts, name='search'),
    path('create/', views.create_post, name='create'),
    path('update/<int:post_id>/', views.update_post, name='update'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),  # Listagem de posts
    path('<int:post_id>/', views.detalhe_post, name='detail'),  # Detalhes do post
]