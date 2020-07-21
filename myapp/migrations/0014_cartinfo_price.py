# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200327_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='price',
            field=models.DecimalField(verbose_name='商品价格', default=1, max_digits=8, decimal_places=2),
            preserve_default=False,
        ),
    ]
