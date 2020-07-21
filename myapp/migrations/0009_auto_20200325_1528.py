# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_comment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(verbose_name='评价类型', max_length=32, default='五星好评', choices=[('五星好评', '五星好评'), ('四星好评', '四星好评'), ('三星好评', '三星中评'), ('二星好评', '二星差评'), ('一星好评', '一星垃圾')]),
        ),
    ]
