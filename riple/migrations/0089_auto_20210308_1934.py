# Generated by Django 3.1.2 on 2021-03-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0088_auto_20210306_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/media/files/defaultdp.jpg', upload_to=''),
        ),
    ]
