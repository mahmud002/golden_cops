# Generated by Django 3.1.7 on 2021-05-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210502_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropguide',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]