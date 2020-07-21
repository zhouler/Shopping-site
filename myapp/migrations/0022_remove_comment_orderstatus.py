# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_order_goods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='orderstatus',
        ),
    ]
