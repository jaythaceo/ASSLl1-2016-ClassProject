# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160114_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccounts',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
