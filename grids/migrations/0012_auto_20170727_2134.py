# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-28 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grids', '0011_auto_20161107_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestate',
            name='current_turn',
            field=models.CharField(choices=[('home', 'Home Team'), ('away', 'Away Team')], default='home', max_length=10),
        ),
    ]
