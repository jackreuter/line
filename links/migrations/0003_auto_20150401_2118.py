# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20150401_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
