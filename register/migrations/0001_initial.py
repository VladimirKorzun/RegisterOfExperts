# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-01 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('expert_type', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpertiseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertiseKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expertise_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ExpertiseClass')),
            ],
        ),
        migrations.CreateModel(
            name='ExpertSpeciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expertise_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ExpertiseKind')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StageAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_begin', models.DateField(verbose_name='Date begin')),
                ('date_end', models.DateField(verbose_name='Date end')),
                ('is_actually', models.BooleanField()),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Expert')),
                ('expert_speciality', models.ManyToManyField(to='register.ExpertSpeciality')),
                ('stage_agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.StageAgency')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Region'),
        ),
        migrations.AddField(
            model_name='expert',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Organization'),
        ),
    ]