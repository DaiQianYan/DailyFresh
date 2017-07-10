# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyFresh_user', '0003_auto_20170705_2028'),
        ('DailyFresh_goods', '0002_auto_20170707_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='DailyFresh_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='DailyFresh_user.UserInfo')),
            ],
        ),
    ]
