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
        'Category', related_name='posts', blank=True
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
