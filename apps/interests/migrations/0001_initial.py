# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(verbose_name=b'2015-07-17')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(verbose_name=b'2015-07-17')),
                ('occupation', models.CharField(max_length=255)),
                ('interests', models.ManyToManyField(to='interests.Interest')),
            ],
        ),
    ]
