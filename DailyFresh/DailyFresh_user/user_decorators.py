# coding = utf-8
from django.shortcuts import redirect
def user_islogin(func):
	def func1(request, *args, **kwargs):
		# 判断是否登录
		if request.session.has_key('uid'):
			# 如果登录,则执行func函数
			return func(request, *args, **kwargs)
		else:
			#如果没登录，则转到login视图/user/login/
			return redirect('/user/login/')
	return func1