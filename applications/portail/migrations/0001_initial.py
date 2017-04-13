# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artefact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('ObjectName', models.CharField(max_length=40, blank=True, null=True, default='No Name')),
                ('GeneralDescription', models.CharField(max_length=40, blank=True, null=True)),
                ('model', models.CharField(max_length=40, blank=True, null=True)),
                ('SerialNumber', models.CharField(max_length=40, blank=True, null=True)),
                ('Manufacturer', models.CharField(max_length=40, blank=True, null=True)),
                ('ManuCountry', models.CharField(max_length=40, blank=True, null=True)),
                ('ManuProvince', models.CharField(max_length=40, blank=True, null=True)),
                ('ManuCity', models.CharField(max_length=40, blank=True, null=True)),
                ('BeginDate', models.CharField(max_length=40, blank=True, null=True)),
                ('EndDate', models.CharField(max_length=40, blank=True, null=True)),
                ('date_qualifier', models.CharField(max_length=40, blank=True, null=True)),
                ('patent', models.CharField(max_length=40, blank=True, null=True)),
                ('NumberOfComponents', models.CharField(max_length=40, blank=True, null=True)),
                ('ArtifactFinish', models.TextField(blank=True, null=True)),
                ('ContextCanada', models.TextField(blank=True, null=True)),
                ('ContextFunction', models.TextField(blank=True, null=True)),
                ('ContextTechnical', models.TextField(blank=True, null=True)),
                ('group1', models.CharField(max_length=40, blank=True, null=True)),
                ('category1', models.CharField(max_length=40, blank=True, null=True)),
                ('subcategory1', models.CharField(max_length=40, blank=True, null=True)),
                ('group2', models.CharField(max_length=40, blank=True, null=True)),
                ('category2', models.CharField(max_length=40, blank=True, null=True)),
                ('subcategory2', models.CharField(max_length=40, blank=True, null=True)),
                ('group3', models.CharField(max_length=40, blank=True, null=True)),
                ('category3', models.CharField(max_length=40, blank=True, null=True)),
                ('subcategory3', models.CharField(max_length=40, blank=True, null=True)),
                ('material', models.CharField(max_length=40, blank=True, null=True)),
                ('Length', models.CharField(max_length=40, blank=True, null=True)),
                ('Width', models.CharField(max_length=40, blank=True, null=True)),
                ('Height', models.CharField(max_length=40, blank=True, null=True)),
                ('Thickness', models.CharField(max_length=40, blank=True, null=True)),
                ('Weight', models.CharField(max_length=40, blank=True, null=True)),
                ('Diameter', models.CharField(max_length=40, blank=True, null=True)),
                ('image', models.URLField(max_length=250, blank=True, null=True)),
                ('thumbnail', models.URLField(max_length=250, blank=True, null=True)),
                ('language', models.CharField(max_length=2, default='EN', choices=[('FR', 'Francais'), ('EN', 'English')])),
            ],
            options={
                'verbose_name': 'Artefact',
                'verbose_name_plural': 'Artefacts',
            },
        ),
    ]
