# Generated by Django 3.1.2 on 2021-02-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0069_auto_20210207_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]
