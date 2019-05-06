from django.contrib import admin

from blog.models import Category, Photo, Post


admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Post)
