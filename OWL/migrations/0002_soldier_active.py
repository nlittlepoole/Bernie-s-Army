# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OWL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldier',
            name='active',
            field=models.IntegerField(default=0),
        ),
    ]
