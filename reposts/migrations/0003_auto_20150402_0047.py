# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposts', '0002_auto_20150402_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repost',
            name='title',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
