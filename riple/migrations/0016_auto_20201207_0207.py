# Generated by Django 3.1.2 on 2020-12-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0015_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='rapunzel.png', upload_to=''),
        ),
    ]
