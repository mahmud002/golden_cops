# Generated by Django 3.1.7 on 2021-05-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210502_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cropguide',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
