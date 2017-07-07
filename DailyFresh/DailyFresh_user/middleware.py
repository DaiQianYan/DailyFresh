# coding = utf-8
from django.http import HttpRequest


class UrlPathMiddleware:
	def process_request(self, request):
		# 只负责记录路径
		path = request.get_full_path()
		path1 = request.path
		# 如果当前请求与用户登录、注册相关，则不需要记录
		if path not in ['/user/register/', 
						'/user/register_handle/', 
						'/user/register_valid/', 
						'/user/login/', 
						'/user/login_handle/', 
						'/user/logout/', ]:
			request.session['url_path'] = path