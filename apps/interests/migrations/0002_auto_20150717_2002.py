# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
