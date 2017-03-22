# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordMatchingModel',
            fields=[
                ('basequestionmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.BaseQuestionModel')),
                ('title', models.CharField(max_length=500)),
                ('score', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('listA', django_mysql.models.ListCharField(models.CharField(max_length=255), max_length=255, size=None)),
                ('listB', django_mysql.models.ListCharField(models.CharField(max_length=255), max_length=255, size=None)),
            ],
            options={
                'verbose_name': 'Word Matching Question',
                'verbose_name_plural': 'Word Matching Questions',
            },
            bases=('app.basequestionmodel',),
        ),
        migrations.AlterField(
            model_name='multiplechoicemodel',
            name='answers',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=255, null=True), blank=True, max_length=255, size=None),
        ),
    ]
