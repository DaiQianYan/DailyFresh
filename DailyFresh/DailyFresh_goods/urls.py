from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^list(\d+)_(\d+)/$', views.goods_list),
	url(r'^(\d+)/$', views.goods_detail),


]