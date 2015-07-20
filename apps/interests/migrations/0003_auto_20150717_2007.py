# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0002_auto_20150717_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
