from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .temp_data import post_data
from .models import Post

def lista_posts(request):
    # posts = Post.objects.all().order_by('-data_postagem')
    context = {"post_list": post_data}
    return render(request, 'posts/index.html', context)

def detalhe_post(request, id):
    post = post_data[id - 1]
    # post = get_object_or_404(Post, id=id)
    return HttpResponse(
        f'Titulo: {post["titulo"]} ; Conteudo {post["conteudo"]}; Data ({post["data_postagem"]})')