from django.conf.urls import url
from . import views


urlpatterns = [
	url('^register/$', views.register),
	url('^register_handle/$', views.register_handle),
	url('^register_valid/$', views.register_valid),
	url('^login/$', views.login),
	url('^login_handle/$', views.login_handle),
	url('^$', views.center),
	url('^order/$', views.order),
	url('^site/$', views.site),
	url('^logout/$', views.logout),
	url('^islogin/$',views.islogin),


]