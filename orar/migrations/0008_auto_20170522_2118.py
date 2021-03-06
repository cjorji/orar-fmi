# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0007_auto_20170522_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar_serie', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='elev',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orar.Serie'),
        ),
        migrations.AddField(
            model_name='grupa',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orar.Serie'),
        ),
    ]
