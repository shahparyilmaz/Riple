# Generated by Django 3.1.2 on 2021-01-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0058_auto_20210130_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, default='default_user.png', upload_to=''),
        ),
    ]
