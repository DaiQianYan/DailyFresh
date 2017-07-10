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


def goods_list(request, tid, pindex, orderby):
    # 商品分类
    t1 = TypeInfo.objects.get(pk = int(tid))
    # 默认排序顺序为id倒序,事实上排序是购物网站最重要的硬实力,像阿里这种都是需要大数据去支持云计算的
    orderby_str = '-id'
    desc = '1'
    if int(orderby) == 2:
        desc = request.GET.get('desc')
        if desc == '1':
            orderby_str = '-gprice'
        else:
            orderby_str = 'gprice'
    elif int(orderby) == 3:
        orderby_str = '-gclick'
    # 推荐新品
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    glist = t1.goodsinfo_set.order_by(orderby_str)
    # 设置分页
    paginator = Paginator(glist, 10)
    pindex1 = int(pindex)
    if pindex1 <= 1:
        pindex1 = 1
    if pindex1 >= paginator.num_pages:
        pindex1 = paginator.num_pages
    page = paginator.page(int(pindex))
    context = {'cart_show' : '0', 'title' : '商品列表', 't1' : t1, 'new_list' : new_list, 'page' : page, 'orderby' : orderby, 'desc' : desc}
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
        response = render(request, 'DailyFresh_goods/detail.html', context)
        # 最近浏览
        ids = request.COOKIES.get('goods_ids', '').split(',')
        if id in ids:
            ids.remove(id)
        ids.insert(0, id)
        if len(ids)>5:
            ids.pop()
        # 用,逗号返回拼接字符串
        response.set_cookie('goods_ids', ','.join(ids), max_age = 60*60*24*7)
        return response
    except Exception as e:
        print(e)
        return render(request, '404.html')