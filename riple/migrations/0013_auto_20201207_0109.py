# Generated by Django 3.1.2 on 2020-12-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0012_auto_20201207_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='rapunzel.png', null=True, upload_to=''),
        ),
    ]
