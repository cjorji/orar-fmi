# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0002_elev_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='elev',
            name='nume',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='nume',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]