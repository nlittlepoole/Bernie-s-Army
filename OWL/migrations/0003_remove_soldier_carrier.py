# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OWL', '0002_soldier_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldier',
            name='carrier',
        ),
    ]
