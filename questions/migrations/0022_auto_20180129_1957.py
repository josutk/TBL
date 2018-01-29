# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-29 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_auto_20180129_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Intermediary', 'Intermediary'), ('Advanced', 'Advanced')], default='basic', help_text='Difficulty level', max_length=15, verbose_name='Level'),
        ),
    ]
