# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0148_stripeaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripeaccount',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]