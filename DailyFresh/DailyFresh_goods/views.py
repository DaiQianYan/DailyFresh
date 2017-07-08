# coding = utf-8
from django.shortcuts import render
from .models import *
# 引入分页函数
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    type_list = TypeInfo.objects.all()
    alist = []
    for types in type_list:
    # 按照id来排，而且是降序来排
        new_list = types.goodsinfo_set.order_by('-id')[0 : 4]
        click_list = types.goodsinfo_set.order_by('-gclick')[0 : 4]
        alist.append({'new_list' : new_list, 'click_list' : click_list, 't1' : types})

    context = {'alist' : alist, 'title' : '首页', 'cart_show' : '0'}
    return render(request, 'DailyFresh_goods/index.html', context)


def goods_list(request, tid, pindex):
    # 商品分类
    t1 = TypeInfo.objects.get(pk = int(tid))
    # 推荐新品
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    glist = t1.goodsinfo_set.order_by('-id')
    # 设置分页
    paginator = Paginator(glist, 15)
    page = paginator.page(int(pindex))
    context = {'cart_show' : '0', 'title' : '商品列表', 't1' : t1, 'new_list' : new_list, 'page' : page}
    return render(request, 'DailyFresh_goods/list.html', context)


def goods_detail(request, id):
    try:
        goods = GoodsInfo.objects.get(pk = int(id))
        # 点击量加1
        goods.gclick += 1
        # 提交数据并保存
        goods.save()
        # 找到当前商品的分类对象, 再找到所有此分类的商品中最新的两种
        new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'cart_show' : '1', 'title': '商品详细信息', 'new_list' : new_list, 'goods' : goods }
        return render(request, 'DailyFresh_goods/detail.html', context)
    except Exception as e:
        print(e)
        return render(request, '404.html')