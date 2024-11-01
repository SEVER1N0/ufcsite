from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .temp_data import post_data
from .models import Post
from .forms import PostForm

def lista_posts(request):
    # posts = Post.objects.all().order_by('-data_postagem')
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    return render(request, 'posts/index.html', context)

def detalhe_post(request, post_id):
    post =  get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_titulo = form.cleaned_data['titulo']
            post_conteudo = form.cleaned_data['conteudo']
            post_poster_url = form.cleaned_data['poster_url']
            post = Post(titulo=post_titulo,
                        conteudo=post_conteudo,
                        poster_url=post_poster_url)
            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/create.html', context)
    
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.titulo = form.cleaned_data['titulo']
            post.conteudo = form.cleaned_data['conteudo']
            post.poster_url = form.cleaned_data['poster_url']
            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))

    else:
        form = PostForm(
            initial={
                'titulo': post.titulo,
                'conteudo': post.conteudo,
                'poster_url': post.poster_url
            })

    context = {'post': post, 'form': form}
    return render(request, 'posts/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)