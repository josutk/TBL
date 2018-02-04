# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-03 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0024_auto_20180203_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Intermediary', 'Intermediary'), ('Advanced', 'Advanced'), ('Basic', 'Basic')], default='basic', help_text='Difficulty level', max_length=15, verbose_name='Level'),
        ),
    ]