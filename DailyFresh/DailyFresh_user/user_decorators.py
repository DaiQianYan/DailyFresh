# coding = utf-8
from django.shortcuts import redirect
def user_islogin(func):
	def func1(request, *args, **kwargs):
		# 判断是否登录
		if request.session.has_key('uid'):
			return func(request, *args, **kwargs)
		else:
			return redirect('/user/login/')
	return func1