# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=15)),
                ('carrier', models.CharField(max_length=100)),
                ('join_date', models.DateTimeField(verbose_name=b'date joined')),
                ('zip_code', models.IntegerField(default=0)),
            ],
        ),
    ]
