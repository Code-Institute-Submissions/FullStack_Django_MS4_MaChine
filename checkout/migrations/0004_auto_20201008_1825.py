# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-08 18:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
