# coding = utf-8
from django.http import HttpRequest


class UrlPathMiddleware:
	def process_request(self, request):
		# 如果当前请求与用户登录、注册相关，则不需要记录
		if request.path not in ['/user/register/', 
						'/user/register_handle/', 
						'/user/register_valid/', 
						'/user/login/', 
						'/user/login_handle/', 
						'/user/logout/', ]:
			# 使用get_full_path()获取详细路径
			request.session['url_path'] = request.get_full_path()