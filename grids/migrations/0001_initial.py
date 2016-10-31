# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-31 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('birth_date', models.DateTimeField(verbose_name='birth date')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defense', models.IntegerField(default=0)),
                ('offense', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grids.Rating'),
        ),
    ]