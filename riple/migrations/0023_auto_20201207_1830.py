# Generated by Django 3.1.2 on 2020-12-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0022_auto_20201207_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='rapunzel.png', null=True, upload_to='images/'),
        ),
    ]
