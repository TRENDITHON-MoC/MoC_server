# Generated by Django 4.2.7 on 2024-02-23 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0001_initial'),
        ('posts', '0004_delete_thumbnailimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='daily',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='daily.daily'),
        ),
    ]
