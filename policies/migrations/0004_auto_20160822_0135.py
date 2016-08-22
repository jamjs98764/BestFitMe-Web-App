# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_auto_20160822_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termcover',
            name='cover_kind',
            field=models.CharField(max_length=20, choices=[('CoverKind.CONSTANT', 'CoverKind.CONSTANT'), ('CoverKind.INCREASING', 'CoverKind.INCREASING'), ('CoverKind.DECREASING', 'CoverKind.DECREASING')], default='CoverKind.CONSTANT'),
        ),
    ]
