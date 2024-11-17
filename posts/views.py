from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_date')
        return context

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

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'posts/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.posts.all()
    return render(request, 'posts/category_detail.html', {'category': category, 'posts': posts})