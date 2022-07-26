# Generated by Django 3.1.7 on 2021-05-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210521_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='intro',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='crop',
            name='title',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='cropguide',
            name='intro',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]
