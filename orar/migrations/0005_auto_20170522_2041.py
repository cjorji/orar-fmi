# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0004_auto_20170521_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='end_hour',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='event',
            name='start_hour',
            field=models.IntegerField(default=8),
        ),
    ]
