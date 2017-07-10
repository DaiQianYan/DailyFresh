from django.db import models
from DailyFresh_user.models import UserInfo


# Create your models here.
class CartInfo(models.Model):
	goods = models.ForeignKey('DailyFresh_goods.GoodsInfo')
	user = models.ForeignKey(UserInfo)
	count = models.IntegerField()