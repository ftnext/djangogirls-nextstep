from django.db.models import Q
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone
from django.views.generic import ListView

from blog.forms import PhotoForm, PostForm
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
        query = self.request.GET.get('keyword')
        if query:
            # スペースでで区切って複数の語が入力されていたらAND検索をする
            keywords = query.split()
            for keyword in keywords:
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
        photo = None
        if request.FILES.get('image'):
            photo_form = PhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo = photo_form.save()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.photo = photo
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
        photo_form = PhotoForm()
    return render(
        request, 'blog/post_edit.html',
        {'form': form, 'photo_form': photo_form}
    )


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    photo = post.photo
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if request.FILES.get('image'):
            # 画像が送信されている場合は、新規保存を試みる
            photo_form = PhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo = photo_form.save()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.photo = photo
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        photo_form = PhotoForm(instance=photo)
    return render(
        request, 'blog/post_edit.html',
        {'form': form, 'photo_form': photo_form}
    )
