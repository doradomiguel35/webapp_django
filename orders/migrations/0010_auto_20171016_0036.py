# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20171013_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(),
        ),
    ]