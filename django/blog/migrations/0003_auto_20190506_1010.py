# Generated by Django 2.2 on 2019-05-06 01:10

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190502_2356_squashed_0003_auto_20190503_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=blog.models.uploaded_image_path, verbose_name='画像')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True, verbose_name='アップロード日')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='post', to='blog.Photo', verbose_name='写真'),
        ),
    ]
