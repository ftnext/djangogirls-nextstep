from django.db.models import Q
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone
from django.views.generic import ListView

from blog.forms import PostForm
from blog.models import Category, Post


class PostList(ListView):
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now())
        category_pk = self.request.GET.get('category')
        if category_pk:
            posts = posts.filter(categories__pk=int(category_pk))
        keyword = self.request.GET.get('keyword')
        if keyword:
            posts = posts.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
