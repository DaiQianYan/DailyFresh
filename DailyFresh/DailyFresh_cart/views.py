# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from .models import *
from DailyFresh_user.models import UserInfo
from DailyFresh_user.user_decorators import user_islogin


# Create your views here.
# 购物车添加功能
def add(request):
    try:    
        uid = request.session.get('uid')
        gid = int(request.GET.get('gid'))
        count = int(request.GET.get('count', '1'))
        cart = CartInfo.objects.filter(user_id = uid, goods_id = gid)
        # 如果用户uid已经购买了商品gid，则将数量+count
        if len(cart) == 1:
            cart1 = cart[0]
            if cart1.goods.gkucun < cart1.count +count:
                return JsonResponse({'isadd':2})
            else:
                cart1.count += count
            cart1.save()
        # 用户uid没有购买gid过商品则添加
        else:
            cart = CartInfo()
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
            cart.save()
        
        return JsonResponse({'isadd' : 1})

    except:
        print(234)
        return JsonResponse({'isadd' : 0})


# 购物车计数功能
def count(request):
    uid = int(request.session.get('uid'))
    count1 = CartInfo.objects.filter(user_id = uid).count()
    return JsonResponse({'count' : count1})


# 编辑购物车功能
def edit(request):
    id = int(request.GET.get('id'))
    count1 = int(request.GET.get('count'))
    cart = CartInfo.objects.get(pk = id)
    cart.count = count1
    cart.save()
    return JsonResponse({'ok': 1})


# 删除商品功能
def delete(request):
    id=int(request.GET.get('id'))
    cart=CartInfo.objects.get(id=id)
    cart.delete()
    return JsonResponse({'ok':1})

# 用修饰器判断是否登录
@user_islogin
def index(request):
    uid=int(request.session.get('uid'))
    cart_list=CartInfo.objects.filter(user_id=uid)
    context={'title':'购物车','cart_list':cart_list}
    return render(request,'DailyFresh_cart/cart.html',context)


# 获取订单
def order(request):
    user=UserInfo.objects.get(pk=request.session.get('uid'))
    cart_ids = request.POST.getlist('cart_id')
    cart_list=CartInfo.objects.filter(id__in=cart_ids)
    context={'title':'提交订单','user':user,'cart_list':cart_list, 'cart_ids':','.join(cart_ids)}
    return render(request,'DailyFresh_cart/order.html', context)