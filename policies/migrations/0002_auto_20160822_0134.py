# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termcover',
            name='cover_kind',
            field=models.CharField(default=['A', 'B', 'C'], max_length=20, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')]),
        ),
    ]
