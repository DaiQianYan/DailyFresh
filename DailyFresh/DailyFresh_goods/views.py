# coding = utf-8
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    type_list = TypeInfo.objects.all()
    alist = []
    for types in type_list:
    # 按照id来排，而且是降序来排
        new_list = types.goodsinfo_set.order_by('-id')[0 : 4]
        click_list = types.goodsinfo_set.order_by('-gclick')[0 : 4]
        alist.append({'new_list' : new_list, 'click_list' : click_list, 't1' : types})

    context = {'list' : alist, 'title' : '首页'}
    return render(request, 'DailyFresh_goods/index.html', context)