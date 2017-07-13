from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^add/$', views.add),
	url(r'^count/$', views.count),
	url(r'^edit/$', views.edit),
	url(r'^del/$',views.delete),
    url(r'^order/$',views.order),

]