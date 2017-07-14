# coding=utf-8
from django.shortcuts import render, redirect
from .models import *
from django.db import transaction
from DailyFresh_cart.models import CartInfo
import datetime


# Create your views here.
'''
下订单操作的编写逻辑:
1.首先创建主表
2.接收购物车id
3.遍历购物车
4.判断库存数量
5.如果库存足够则:
    5.1创建详单
    5.2修改数量
    5.3删除购物车
6.如果库存不足则回滚
7.计算总价
'''


@transaction.atomic
def do_order(request):
    sid = transaction.savepoint()
    is_commit = True
    try:
        # 获取请求的购物车信息
        cart_ids = request.POST.get('c_ids').split(',')
        # 创建订单主表
        main = OrderMain()
        time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user_id = request.session.get('uid')
        main.orderid = '%s%d'%(time_str, user_id)
        main.user_id = user_id
        main.save()
        # 逐个遍历购物车中的商品,进行数量的判断,如果库存足够则添加到详单,如果库存不够则购买失败回滚
        cart_list = CartInfo.objects.filter(id_in = cart_ids)
        total = 0
        for cart in cart_list:
            if cart.count <= cart.goods.gkucun:
                # 如果库存足够则添加到详单
                detail = OrderDetail()
                detail.order = main
                detail.goods = cart.goods
                detail.count = cart.count
                detail.price = cart.goods.gprice
                # 计算总价
                total += cart.count*cart.goods.gprice
                detail.save()
                # 修改库存
                cart.goods.kucun -= cart.count
                cart.goods.save()
                # 删除购物车
                cart.delete()
            else:
                # 如果库存不够则购买失败回滚
                transaction.savepoint_rollback(sid)
                is_commit = False
                break
        if is_commit:
            main.total = total
            main.save()
            transaction.savepoint_commit(sid)
    except:
        is_commit = False
        transaction.savepoint_rollback(sid)
    # 返回response对象
    if is_commit:
        return redirect('/user/order/')
    else:
        return redirect('/cart/')
        
