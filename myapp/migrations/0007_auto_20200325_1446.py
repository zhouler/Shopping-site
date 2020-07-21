# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200325_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='orderstatus',
            field=models.ForeignKey(to='myapp.Order'),
        ),
    ]
