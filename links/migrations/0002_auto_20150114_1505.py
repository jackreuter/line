# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='content',
        ),
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(default='google.com'),
            preserve_default=False,
        ),
    ]
