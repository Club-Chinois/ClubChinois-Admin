# Generated by Django 3.2 on 2021-05-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0018_auto_20210518_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='vol',
            name='isPart',
            field=models.BooleanField(default=0),
        ),
    ]