# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('system_id', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('series', models.CharField(max_length=200)),
                ('episode', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('synopsys', models.CharField(max_length=200)),
                ('audience', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=200)),
                ('primo_url', models.CharField(max_length=200)),
                ('thumbnail_url', models.CharField(max_length=200)),
                ('entry_id', models.CharField(max_length=200)),
                ('video_url', models.CharField(max_length=200)),
                ('clean_records', models.CharField(max_length=200)),
            ],
        ),
    ]
