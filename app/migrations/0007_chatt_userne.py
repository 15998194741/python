# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-04-14 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_chatt'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatt',
            name='userne',
            field=models.CharField(default=1, max_length=128, verbose_name='凭证'),
            preserve_default=False,
        ),
    ]
