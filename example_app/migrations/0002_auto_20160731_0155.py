# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 01:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Secrets',
            new_name='Secret',
        ),
    ]