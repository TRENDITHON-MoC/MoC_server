# Generated by Django 4.2.7 on 2024-02-20 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='hashtag',
            table='hashtag',
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='postimage',
            table='post_image',
        ),
        migrations.AlterModelTable(
            name='thumbnailimage',
            table='thumbnail_image',
        ),
    ]