# Generated by Django 3.1.7 on 2021-05-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210501_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50)),
                ('details', models.TextField(blank=True, max_length=1000)),
                ('price', models.TextField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='home/images')),
            ],
        ),
    ]