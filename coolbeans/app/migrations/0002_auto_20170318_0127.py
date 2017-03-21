# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 01:27
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
            name='CrosswordQuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('direction', models.CharField(max_length=500)),
                ('length', models.PositiveIntegerField()),
                ('x', models.PositiveIntegerField()),
                ('y', models.PositiveIntegerField()),
                ('clue', models.CharField(max_length=500)),
                ('score', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('answer', models.CharField(max_length=500)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.BaseQuestionModel')),
            ],
            options={
                'verbose_name': 'Crossword Question',
                'verbose_name_plural': 'Crossword Questions',
            },
        ),
        migrations.AlterField(
            model_name='multiplechoicemodel',
            name='answers',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=255, null=True), blank=True, max_length=255, size=None),
        ),
    ]
