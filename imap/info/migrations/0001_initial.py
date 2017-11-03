# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload/room/')),
            ],
        ),
        migrations.CreateModel(
            name='ImageService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload/content/')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubTherapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='upload/Package/Therapy/')),
            ],
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='subtherapy',
            name='therapy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Therapy'),
        ),
        migrations.AddField(
            model_name='imageservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Service'),
        ),
        migrations.AddField(
            model_name='imageroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Room'),
        ),
    ]
