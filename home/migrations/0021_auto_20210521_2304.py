# Generated by Django 3.1.7 on 2021-05-22 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='ctop',
            new_name='crop',
        ),
    ]
