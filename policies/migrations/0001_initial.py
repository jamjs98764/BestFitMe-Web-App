# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ForeverCover',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthOrder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('hospital_admission_cover', models.BooleanField()),
                ('long_term_care', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='HealthPolicy',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('clinic_gp_cover', models.IntegerField()),
                ('accident_cover', models.IntegerField()),
                ('company', models.OneToOneField(to='policies.Company')),
            ],
        ),
        migrations.CreateModel(
            name='LifeOrder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cover_amount', models.FloatField()),
                ('premum_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LifePolicy',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('mortage', models.IntegerField()),
                ('children_education_fund', models.IntegerField()),
                ('critical_cover', models.IntegerField()),
                ('company', models.OneToOneField(to='policies.Company')),
            ],
        ),
        migrations.CreateModel(
            name='TermCover',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cover_kind', models.CharField(choices=[('CONSTANT', 'CONSTANT'), ('INCREASING', 'INCREASING'), ('DECREASING', 'DECREASING')], max_length=20, default='CONSTANT')),
                ('cover_level', models.IntegerField()),
                ('term_length', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lifeorder',
            name='policy',
            field=models.OneToOneField(to='policies.LifePolicy'),
        ),
        migrations.AddField(
            model_name='healthorder',
            name='policy',
            field=models.OneToOneField(to='policies.HealthPolicy'),
        ),
    ]
