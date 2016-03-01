# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 19:30
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0068_worker_scope'),
        ('random2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='config', to='crowdsourcing.Worker')),
            ],
        ),
    ]