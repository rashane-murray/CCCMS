# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 20:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubSetup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='daysHeld',
        ),
        migrations.RemoveField(
            model_name='club',
            name='meetingsNum',
        ),
        migrations.RemoveField(
            model_name='club',
            name='numDaysHeld',
        ),
    ]