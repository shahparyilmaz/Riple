# Generated by Django 3.1.2 on 2021-01-29 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riple', '0059_auto_20210130_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_pic',
            new_name='pic',
        ),
    ]
