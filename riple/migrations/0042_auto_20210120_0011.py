# Generated by Django 3.1.2 on 2021-01-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0041_auto_20210119_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
