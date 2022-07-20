# Generated by Django 3.1.7 on 2021-05-22 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20210522_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]