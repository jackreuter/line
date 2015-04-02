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
                ('title', models.CharField(max_length=255, null=True)),
                ('url', models.URLField()),
                ('hotness', models.IntegerField()),
                ('posted_by', models.ForeignKey(related_name='links', to=settings.AUTH_USER_MODEL)),
                ('tag1', models.ForeignKey(related_name='links_tagged_in_1', to=settings.AUTH_USER_MODEL, null=True)),
                ('tag2', models.ForeignKey(related_name='links_tagged_in_2', to=settings.AUTH_USER_MODEL, null=True)),
                ('tag3', models.ForeignKey(related_name='links_tagged_in_3', to=settings.AUTH_USER_MODEL, null=True)),
                ('tag4', models.ForeignKey(related_name='links_tagged_in_4', to=settings.AUTH_USER_MODEL, null=True)),
                ('tag5', models.ForeignKey(related_name='links_tagged_in_5', to=settings.AUTH_USER_MODEL, null=True)),
                ('tag6', models.ForeignKey(related_name='links_tagged_in_6', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created_at', 'title'],
            },
            bases=(models.Model,),
        ),
    ]
