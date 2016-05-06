# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-06 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0074_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=8192)),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('task_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_feedback', to='crowdsourcing.TaskWorker')),
            ],
            options={
                'ordering': ['-created_timestamp'],
            },
        ),
        migrations.AlterField(
            model_name='conversationrecipient',
            name='status',
            field=models.SmallIntegerField(choices=[(1, b'Open'), (2, b'Minimized'), (3, b'Closed'), (4, b'Muted')], default=1),
        ),
    ]
