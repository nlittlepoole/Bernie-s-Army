# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OWL', '0003_remove_soldier_carrier'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldier',
            name='carrier',
            field=models.CharField(default='Sprint', max_length=100),
            preserve_default=False,
        ),
    ]
