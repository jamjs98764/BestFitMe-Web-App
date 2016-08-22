# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0002_auto_20160822_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termcover',
            name='cover_kind',
            field=models.CharField(default=['A.B', 'B', 'C'], choices=[('A.B', 'A.B'), ('B', 'B'), ('C', 'C')], max_length=20),
        ),
    ]
