# Generated by Django 4.2.7 on 2024-02-22 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_hashtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='located',
        ),
    ]