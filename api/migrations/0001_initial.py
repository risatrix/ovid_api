# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('full_name', models.CharField(max_length=128, unique=True)),
                ('abbreviation', models.CharField(max_length=128, unique=True)),
                ('slug', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('book_index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_index', models.IntegerField()),
                ('text', models.CharField(max_length=500, unique=True)),
                ('meter', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('poem_index', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('abbreviation', models.CharField(max_length=128, unique=True)),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Author')),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='poem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Poem'),
        ),
        migrations.AddField(
            model_name='book',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Work'),
        ),
    ]