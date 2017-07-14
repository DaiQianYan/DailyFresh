# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyFresh_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordermain',
            name='total',
            field=models.DecimalField(max_digits=8, default=0, decimal_places=2),
        ),
    ]
