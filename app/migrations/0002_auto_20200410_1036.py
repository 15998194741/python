# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-04-10 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='telephone',
            field=models.CharField(max_length=11, verbose_name='电话号码'),
        ),
    ]