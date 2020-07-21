# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200304_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='quantity',
            field=models.IntegerField(verbose_name='数量', default=1),
        ),
    ]
