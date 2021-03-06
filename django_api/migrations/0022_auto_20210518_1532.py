# Generated by Django 3.2 on 2021-05-18 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0021_auto_20210518_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='ane',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ane',
            name='isFreeze',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='ane',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ane',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ane',
            name='stop_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
