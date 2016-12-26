# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(auto_created=True, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок')),
                ('content', models.TextField(max_length=400, verbose_name='Текст объявления')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Destrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Район')),
            ],
            options={
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.AddField(
            model_name='ad',
            name='area',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.Destrict', verbose_name='Район'),
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Category', verbose_name='Категория'),
        ),
    ]