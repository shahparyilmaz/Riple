# Generated by Django 3.1.2 on 2021-01-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0033_auto_20201208_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=18, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/default_user.png', upload_to=''),
        ),
    ]
