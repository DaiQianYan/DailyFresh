# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='goods/')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gclick', models.IntegerField()),
                ('gunit', models.CharField(max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
                ('gsubtitle', models.CharField(max_length=200)),
                ('gkucun', models.IntegerField(default=100)),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('ttile', models.CharField(max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='DailyFresh_goods.TypeInfo'),
        ),
    ]
