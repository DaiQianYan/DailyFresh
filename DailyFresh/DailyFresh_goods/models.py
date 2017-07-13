from django.db import models
# 导入富文本编辑器
from tinymce.models import HTMLField


# Create your models here.
# 定义商品大类
class TypeInfo(models.Model):
	ttitle = models.CharField(max_length = 10)
	isDelete = models.BooleanField(default = False)

	def __str__(self):
		return self.ttitle.encode('utf-8')


# 定义商品详细信息,按照给定的goods.sql进行排序
class GoodsInfo(models.Model):
	# 商品标题
	gtitle = models.CharField(max_length = 20)
	gpic = models.ImageField(upload_to = 'goods/')
	gprice = models.DecimalField(max_digits = 5, decimal_places = 2)
	gclick = models.IntegerField()
	gunit = models.CharField(max_length = 10)
	isDelete = models.BooleanField(default = False)
	gsubtitle = models.CharField(max_length = 200)
	# 库存量剩余数
	gkucun = models.IntegerField(default = 100)
	gcontent = HTMLField()
	gtype = models.ForeignKey('TypeInfo')