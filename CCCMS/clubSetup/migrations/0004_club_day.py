# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubSetup', '0003_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='day',
            field=models.IntegerField(default=0),
        ),
    ]
