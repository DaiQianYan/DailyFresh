# coding=utf-8
from django.db import models
from DailyFresh_user.models import UserInfo
from DailyFresh_goods.models import GoodsInfo


# Create your models here.
class OrderMain(models.Model):
	orderid = models.CharField(max_length = 20, primary_key = True)
	order_time = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(UserInfo)
	total =models.DecimalField(max_digits = 8, decimal_places = 2, default = 0)
	state = models.IntegerField(default = 0)


class OrderDetail(models.Model):
	order = models.ForeignKey(OrderMain)
	goods = models.ForeignKey(GoodsInfo)
	count = models.IntegerField()
	price = models.DecimalField(max_digits = 5, decimal_places = 2)