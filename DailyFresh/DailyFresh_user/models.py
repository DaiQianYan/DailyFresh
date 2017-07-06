# coding = utf-8
from django.db import models


# Create your models here.
# 1.0创建用户信息模型
class UserInfo(models.Model):
	uname = models.CharField(max_length = 20)
	# sha1加密
	upwd = models.CharField(max_length = 40)
	umail = models.CharField(max_length = 30)
	# 设置收货人信息consignee,需要设置默认值,不然如果不输入内容会自动提交,不会判断
	uconsignee = models.CharField(default = '',max_length = 20)
	uaddress = models.CharField(default = '', max_length = 100)
	# 设置邮编postcode信息
	upostcode = models.CharField(default = '', max_length = 6)
	uphone = models.CharField(default = '', max_length = 11)


