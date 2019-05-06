from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name='作成者'
    )
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    categories = models.ManyToManyField(
        'Category', related_name='posts', blank=True,
        verbose_name='カテゴリ',
        help_text='複数選択できます。controlキー（Macではcommandキー）を使ってください'
    )
    photo = models.ForeignKey(
        'Photo', on_delete=models.PROTECT,
        verbose_name='写真', related_name='post', blank=True, null=True
    )
    created_date = models.DateTimeField('作成日', default=timezone.now)
    published_date = models.DateTimeField('公開日', blank=True, null=True)

    class Meta:
        ordering = ['-published_date', '-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


def uploaded_image_path(instance, filename):
    # アップロード先：MEDIA_ROOT/photos/<uuid>.png
    image_extension = filename.split('.')[-1]
    return f'photos/{instance.id}.{image_extension}'


class Photo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    image = models.ImageField('画像', upload_to=uploaded_image_path)
    uploaded_date = models.DateTimeField('アップロード日', auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
