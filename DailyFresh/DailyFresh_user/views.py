# coding = utf-8
from django.shortcuts import render, redirect
# 为了register_valid判断引入JsonResponse
from django.http import JsonResponse
from .models import UserInfo
# 导入sha1模块进行加密
from hashlib import sha1
import datetime
from . import user_decorators
# 从goods模块引入商品信息GoodsInfo
from DailyFresh_goods.models import GoodsInfo


# Create your views here.
# 定义注册页面
def register(request):
    context = {'title' : '注册', 'top' : '0'}
    return render(request, 'DailyFresh_user/register.html', context)


# 定义注册页面数据处理方法
def register_handle(request):
    # 接收用户请求,获取用户输入数据
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    ucpwd = post.get('user_cpwd')
    umail = post.get('user_mail')

    # 由于来源于客户端的验证可能不准确,所以在服务器端最好再写一遍验证
    context = {}
    if len(uname) < 5 or len(uname) > 20:
        context['error'] = '请输入5-20个字符的用户名'
        context['uname'] = uname
        return render(request, 'DailyFresh_user/register.html', context)

    # 最后确定没有问题,才会重定向跳转到登录页面
    else:
        # 使用sha1方法加密
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        upwd_sha1 = s1.hexdigest()

        # 创建对象,传参,向数据库中保存数据
        user = UserInfo()
        user.uname = uname
        # 这里需要把加密的密码传给数据库,不然就是明码
        user.upwd = upwd_sha1
        user.umail = umail
        user.save()

        # 重定向自动跳转到登陆页面
        return redirect('/user/login/')


# 用ajax判断用户名是否存在
def register_valid(request):
    # 接收用户名
    uname = request.GET.get('uname')
    # 查询当前用户名的个数.统计查到的结果为个数,因为并不关心对象,只关心有没有
    data = UserInfo.objects.filter(uname = uname).count()
    # 构造字典返回json{'vaild': data}
    context = {'valid' : data}
    return JsonResponse(context)


# 登陆login
def login(request):
    # 如果又储存的用户名,从cookie中取到赋予uname
    uname = request.COOKIES.get('uname', '')
    context = {'title' : '登录', 'uname' : uname, 'top' : '0'}
    return render(request, 'DailyFresh_user/login.html', context)


# 登录确认,先写逻辑,再写具体的代码来完善逻辑.
def login_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    # 记住用户.存cookie还是sension主要取决于数据是否保密
    ujz = post.get('user_jz', 0)

    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd_sha1 = s1.hexdigest()

    # 为了下面的判断做准备,共有的部分是title
    context = {'title' : '登录', 'uname' : uname, 'upwd' : upwd, 'top' : '0'}

    # 如果没有查到数据则返回[],如果查询到了数据则返回[UserInfo]
    result = UserInfo.objects.filter(uname = uname)
    if len(result) == 0:
        # 用户名不存在
        context['error_name'] = '用户名错误'
        return render(request, 'DailyFresh_user/login.html', context)

    else:
        if result[0].upwd == upwd_sha1:
            # 登陆成功.response是一个简写函数
            response = redirect(request.session.get('url_path', '/'))
            request.session['uid'] = result[0].id
            # 储存登录名
            request.session['uname'] = result[0].uname
            # 记住用户名
            # 所有从request请求报文得来的数据都是字符串
            if ujz == '1':
                # 设置cookies过期时间为14天
                response.set_cookie('uname', uname, expires = datetime.datetime.now() + datetime.timedelta(days = 14))
            # 如果未勾选记住用户则不记住
            else:
                response.set_cookie('uname', '', max_age = -1)

            return response


        else: 
            # 密码错误
            context['error_pwd'] = '密码错误'
            return render(request, 'DailyFresh_user/login.html', context)


@user_decorators.user_islogin
# 登陆成功后的用户中心视图
def center(request):
    # 查询当前登录的用户对象
    user = UserInfo.objects.get(pk = request.session['uid'])
    # 查询最近浏览
    ids = request.COOKIES.get('goods_ids', '').split(',')[:-1]
    glist = []
    for id in ids:
        glist.append(GoodsInfo.objects.get(id=id))
    context = {'user' : user, 'glist' : glist}
    return render(request, 'DailyFresh_user/center.html', context)


@user_decorators.user_islogin
# 订单视图
def order(request):
    context = {}
    return render(request, 'DailyFresh_user/order.html', context)


@user_decorators.user_islogin
# 收货地址视图
def site(request):
    # 查询当前登录的用户对象
    user = UserInfo.objects.get(pk = request.session['uid'])
    # POST请求,接收用户数据.POST说明用户需要新增数据
    if request.method == 'POST':
        post = request.POST
        uconsignee = post.get('uconsignee')
        uaddress = post.get('uaddress')
        upostcode= post.get('upostcode')
        uphone = post.get('uphone')

        # 向数据库传数据
        user.uconsignee = uconsignee
        user.uaddress = uaddress
        user.upostcode = upostcode
        user.uphone = uphone
        # 向数据库提交
        user.save()
    
    context = {'user' : user}
    return render(request, 'DailyFresh_user/site.html', context)

    # # get请求,查数据,不执行新增数据的代码
    # else:


def logout(request):
    request.session.flush()
    return redirect('/user/login/')