# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('year', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('from_year', models.SmallIntegerField()),
                ('to_year', models.SmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='asset',
            name='series',
            field=models.ForeignKey(to='video.Season'),
        ),
        migrations.AddField(
            model_name='season',
            name='series',
            field=models.ForeignKey(to='video.Series'),
        ),
    ]
