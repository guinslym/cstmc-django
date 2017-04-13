# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artefact',
            name='IDNO',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
    ]
