# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('is_resolved', models.BooleanField(default=False, verbose_name='Resolved?')),
            ],
        ),
    ]