# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyFresh_user', '0002_auto_20170705_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='umail',
            field=models.CharField(max_length=30),
        ),
    ]
