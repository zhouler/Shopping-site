# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20200325_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='store',
            field=models.ForeignKey(default=1, related_name='store', to='myapp.Login'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartinfo',
            name='user',
            field=models.ForeignKey(related_name='user', to='myapp.Login'),
        ),
    ]
