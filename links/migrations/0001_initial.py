# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('posted_by', models.ForeignKey(related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'title'],
            },
            bases=(models.Model,),
        ),
    ]
