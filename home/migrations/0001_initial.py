# Generated by Django 3.1.7 on 2021-04-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50)),
                ('std_id', models.TextField(blank=True, max_length=50)),
                ('department', models.TextField(blank=True, max_length=50)),
            ],
        ),
    ]
