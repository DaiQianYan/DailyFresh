# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyFresh_goods', '0002_auto_20170707_1702'),
        ('DailyFresh_user', '0003_auto_20170705_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='DailyFresh_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('orderid', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(max_digits=8, decimal_places=2)),
                ('user', models.ForeignKey(to='DailyFresh_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='DailyFresh_order.OrderMain'),
        ),
    ]
