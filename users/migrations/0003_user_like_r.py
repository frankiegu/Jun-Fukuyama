# Generated by Django 3.0 on 2019-12-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_delete_likeship'),
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_r',
            field=models.ManyToManyField(to='video.Video'),
        ),
    ]