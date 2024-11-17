from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('search/', views.search_posts, name='search'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),

]