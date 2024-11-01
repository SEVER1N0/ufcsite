from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:index')
    
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:index')


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:index')