# Generated by Django 3.1.7 on 2021-05-21 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210518_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='name',
        ),
        migrations.AddField(
            model_name='crop',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]