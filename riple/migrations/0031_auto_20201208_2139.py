# Generated by Django 3.1.2 on 2020-12-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0030_auto_20201208_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_user.png', upload_to=''),
        ),
    ]
