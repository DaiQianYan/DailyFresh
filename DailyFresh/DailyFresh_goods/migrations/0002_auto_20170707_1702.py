# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyFresh_goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeinfo',
            old_name='ttile',
            new_name='ttitle',
        ),
    ]
