# Generated by Django 3.1.2 on 2021-01-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0034_auto_20210117_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_user.png', upload_to=''),
        ),
    ]
