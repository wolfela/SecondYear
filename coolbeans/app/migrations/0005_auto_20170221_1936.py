# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170212_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mcqquestionmodel',
            options={'verbose_name': 'Multiple Choice Question', 'verbose_name_plural': 'Multiple Choice Questions'},
        ),
        migrations.RenameField(
            model_name='questionmodel',
            old_name='parent',
            new_name='display_with',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='mcqquestionmodel',
            name='answers',
            field=django_mysql.models.ListCharField(models.CharField(max_length=255), default=None, max_length=255, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mcqquestionmodel',
            name='correct',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mcqquestionmodel',
            name='score',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mcqquestionmodel',
            name='title',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='GapFillQuestionModel',
            fields=[
                ('questionmodel_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='app.QuestionModel')),
                ('text', django_bleach.models.BleachField()),
            ],
            options={
                'abstract': False,
            },
            bases=('app.questionmodel',),
        ),
        migrations.CreateModel(
            name='TrueFalseQuestionModel',
            fields=[
                ('questionmodel_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='app.QuestionModel')),
                ('title', models.CharField(max_length=500)),
                ('answer', models.BooleanField()),
                ('score', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'True or False Question',
                'verbose_name_plural': 'True or False Questions',
            },
            bases=('app.questionmodel',),
        ),
        migrations.CreateModel(
            name='WordMatchingQuestionModel',
            fields=[
                ('questionmodel_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='app.QuestionModel')),
                ('title', models.CharField(max_length=500)),
                ('score', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Word Matching Question',
                'verbose_name_plural': 'Word Matching Questions',
            },
            bases=('app.questionmodel',),
        ),
        migrations.CreateModel(
            name='WordScrambleQuestionModel',
            fields=[
                ('questionmodel_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='app.QuestionModel')),
                ('title', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('scrambled_sentence', models.CharField(max_length=500)),
                ('score', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Word Scramble Question',
                'verbose_name_plural': 'Word Scramble Questions',
            },
            bases=('app.questionmodel',),
        ),
    ]
