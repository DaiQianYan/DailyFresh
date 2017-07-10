from django.conf.urls import url
from . import views
from .search_view import *


urlpatterns = [
	url(r'^$', views.index),
	url(r'^list(\d+)_(\d+)_(\d+)/$', views.goods_list),
	url(r'^(\d+)/$', views.goods_detail),
	url(r'^search/$', MySearchView.as_view())


]