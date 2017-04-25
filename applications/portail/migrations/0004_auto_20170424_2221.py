# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portail', '0003_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artefact',
            name='ObjectName',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
    ]
