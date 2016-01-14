# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 12:05
from __future__ import unicode_literals

import accounts.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_useraccounts_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccounts',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2016, 1, 14, 12, 5, 37, 367066, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccounts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='useraccounts',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2016, 1, 14, 12, 5, 48, 838883, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='password',
            field=models.CharField(max_length=15),
        ),
    ]
