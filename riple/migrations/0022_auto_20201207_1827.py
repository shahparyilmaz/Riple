# Generated by Django 3.1.2 on 2020-12-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0021_auto_20201207_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='rapunzel.png', upload_to='images/'),
        ),
    ]
