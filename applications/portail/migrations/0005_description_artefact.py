# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portail', '0004_auto_20170424_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='artefact',
            field=models.ForeignKey(default=1, to='portail.Artefact'),
            preserve_default=False,
        ),
    ]
