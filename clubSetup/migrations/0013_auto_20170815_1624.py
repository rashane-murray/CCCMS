# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubSetup', '0012_auto_20170815_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicyear',
            old_name='initalCreate',
            new_name='updateStudentList',
        ),
    ]
