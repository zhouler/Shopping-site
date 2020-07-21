# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_balance_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartinfo',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='cartinfo',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cartinfo',
            name='title',
        ),
    ]
