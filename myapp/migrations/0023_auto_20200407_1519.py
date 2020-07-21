# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_comment_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='order',
            field=models.ForeignKey(default=1, to='myapp.Order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(verbose_name='评价类型', max_length=32, default='五星好评', choices=[('五星好评', '五星好评'), ('四星好评', '四星好评'), ('三星中评', '三星中评'), ('二星差评', '二星差评'), ('一星差评', '一星差评')]),
        ),
    ]
