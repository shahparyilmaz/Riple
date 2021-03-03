# Generated by Django 3.1.2 on 2021-01-21 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('riple', '0048_auto_20210122_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendlist',
            name='friend',
        ),
        migrations.AddField(
            model_name='friendlist',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
