# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_uservalues_firstlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservalues',
            name='firstLogin',
            field=models.BooleanField(default=True),
        ),
    ]
