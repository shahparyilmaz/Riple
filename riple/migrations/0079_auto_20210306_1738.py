# Generated by Django 3.1.2 on 2021-03-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0078_auto_20210306_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(upload_to='files/'),
        ),
    ]
