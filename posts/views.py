from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .temp_data import post_data
from .models import Post

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
        post_titulo = request.POST['titulo']
        post_conteudo = request.POST['conteudo']
        post_poster_url = request.POST['poster_url']
        post = Post(titulo=post_titulo,
                      conteudo=post_conteudo,
                      poster_url=post_poster_url)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})
    
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.titulo = request.POST['titulo']
        post.conteudo = request.POST['conteudo']
        post.poster_url = request.POST['poster_url']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'posts/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)