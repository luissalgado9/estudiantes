# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-11 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=2)),
                ('correo', models.EmailField(max_length=30)),
                ('carrera', models.CharField(max_length=30)),
                ('turno', models.CharField(max_length=20)),
            ],
        ),
    ]