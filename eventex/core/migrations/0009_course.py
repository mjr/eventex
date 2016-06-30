# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-30 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160630_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Talk')),
                ('slots', models.IntegerField(verbose_name='vagas')),
            ],
            options={
                'verbose_name_plural': 'cursos',
                'verbose_name': 'curso',
            },
            bases=('core.talk',),
        ),
    ]