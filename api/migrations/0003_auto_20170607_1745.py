# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_restaurant_user_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.FloatField(default=37.791),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.FloatField(default=-122.3933),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='place_id',
            field=models.CharField(max_length=500),
        ),
    ]
