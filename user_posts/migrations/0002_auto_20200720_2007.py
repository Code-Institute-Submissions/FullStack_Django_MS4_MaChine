# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-20 20:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_posts',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
