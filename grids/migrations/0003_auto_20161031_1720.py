# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-01 00:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grids', '0002_gameboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameboard',
            old_name='gameboard_cols',
            new_name='cols',
        ),
        migrations.RenameField(
            model_name='gameboard',
            old_name='gameboard_rows',
            new_name='rows',
        ),
    ]
