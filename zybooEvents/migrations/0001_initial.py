# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 00:50
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HappyPubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='PubEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fromDatetime', models.DateTimeField()),
                ('toDatetime', models.DateTimeField()),
                ('pubName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zybooEvents.HappyPubs')),
            ],
        ),
    ]