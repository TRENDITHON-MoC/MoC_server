# Generated by Django 4.2.7 on 2024-02-22 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_located'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ThumbnailImage',
        ),
    ]
