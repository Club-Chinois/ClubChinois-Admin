# Generated by Django 3.2 on 2021-05-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=20),
        ),
    ]
