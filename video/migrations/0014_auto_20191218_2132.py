# Generated by Django 3.0 on 2019-12-18 13:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0013_auto_20191218_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='like',
            field=models.ManyToManyField(default=0, null=True, related_name='ssssss', to=settings.AUTH_USER_MODEL, verbose_name='点赞数'),
        ),
    ]
