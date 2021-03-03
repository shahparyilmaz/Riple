# Generated by Django 3.1.2 on 2021-01-21 18:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('riple', '0049_auto_20210122_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendlist',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='friendlist',
            name='following',
        ),
        migrations.AddField(
            model_name='friendlist',
            name='friend',
            field=models.ManyToManyField(blank=True, null=True, related_name='Userfriend', to=settings.AUTH_USER_MODEL),
        ),
    ]
