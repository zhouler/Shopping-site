import uuid
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator
import datetime
import time
import random

from django.shortcuts import render, redirect
from django.db import transaction

# 注册用户
def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    elif request.method == "POST":

        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(username, password2, password1, 7777777777777)
        L = Login.objects.filter(is_delete=0, username=username).first()
        if L:
            return render(request, 'register.html', context={"flog": 2})  # flog=2 用户已经存在

        if password1 != password2:
            return render(request, 'register.html', context={"flog": 1})  # flog=1两次密码不一致！

        t = Login()  # 实例化
        t.username = username  # 增加新的字段
        password1 = make_password(password1)
        t.password = password1  # 增加新的字段
        t.save()  # 保存

        b = Balance()
        b.user = t
        b.save()
        return redirect("/login")


# 登录
def login(request):
    if request.method == "GET":

        return render(request, "login.html")

    elif request.method == "POST":

        user_info = request.POST
        username = user_info.get("username")

        password = user_info.get("password")

        L = Login.objects.filter(is_delete=0, username=username).first()
        # 把没有被逻辑删除的用户取出来

        if not L:  # 如果没有该用户
            return render(request, 'login.html', context={"flog": 1})  # 返回登录页面， 用户不存在

        ret = check_password(password, L.password)  # 解码

        if ret:
            token = str(uuid.uuid4())  # 生成随机的字符串token
            request.session['token'] = token  # 保存token和username到浏览器session
            request.session['username'] = username

            Token.objects.update_or_create(user=L, defaults={'token': token})

            return redirect("../")

        return render(request, 'login.html', context={"flog": 1})  # 返回登录页面，显示账号密码错误


def index(request):
    now_time = datetime.datetime.now()

    # 本月销量top1-4商品
    month_top_goods0_3 = Goods.objects.filter(created_time__month=now_time.month).order_by('-sales')[:4]
    month_top_goods4_7 = Goods.objects.filter(created_time__month=now_time.month).order_by('-sales')[4:8]

    month_look_top_goods0_3 = Goods.objects.filter(created_time__month=now_time.month).order_by('-look')[:4]
    month_look_top_goods4_7 = Goods.objects.filter(created_time__month=now_time.month).order_by('-look')[4:8]


    context = {
        "month_top_goods0_3": month_top_goods0_3,
        "month_top_goods4_7": month_top_goods4_7,
        "month_look_top_goods0_3": month_look_top_goods0_3,
        "month_look_top_goods4_7": month_look_top_goods4_7,

    }

    return render(request, 'index.html', context=context)


def detailpage(request, good_id):
    good = Goods.objects.filter(id=good_id).first()

    Goods.increase_look(good)  # 增加浏览量

    comment = Comment.objects.filter(goods=good)
    return render(request, "Detail.html", context={"good": good,
                                                   "comment": comment
                                                   })


def personal_shopcar(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    car = CartInfo.objects.filter(user=L)

    return render(request, "personal_shopcar.html", context={"car": car,
                                                             })


"""利用ajax加入购物车"""
def join_gouwuche(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")  # 获取浏览器中session里面的username
    id = request.POST.get("id")  # 获取商品的id
    number = request.POST.get("number")  # 获取商品的id

    L = Login.objects.filter(username=username).first()
    G = Goods.objects.filter(id=id).first()

    # G.user_id 获取商品的 卖家 的id
    store = Login.objects.filter(id=G.user_id).first()  # 去用户表里面找卖家对象
    # 建立购物车对象,update_or_create如果有就更新，没有就建立
    try:
        CartInfo.objects.update_or_create(user=L,goods=G,
                                          defaults={'ccount': number, 'store': store })
                                                                             # 'title': G.title, "price": G.price,
    except:
        return HttpResponse("error")

    return HttpResponse("ok")

"""利用ajax移除购物车"""
def quxiao_gouwuche(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")  # 获取浏览器中session里面的username
    id = request.POST.get("id")  # 获取商品的id

    L = Login.objects.filter(username=username).first()
    G = Goods.objects.filter(id=id).first()
    try:
        CartInfo.objects.filter(user=L,goods=G).delete()
    except:
        return HttpResponse("error")

    return HttpResponse("ok")


"""利用ajax下订单"""
def place_an_order(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误，不能加入购物车")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")  # 获取浏览器中session里面的username

    id = request.POST.get("id")  # 获取商品的id
    number = int(request.POST.get("number"))  # 获取商品的数量
    price = int(request.POST.get("price"))  # 获取商品的价格
    L = Login.objects.filter(username=username).first()
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    ret = time + str(username[0:3])  # 随机生成一个1000到9999的int类型的数

    A = Adress.objects.filter(user=L).first()  # 获取该用户默认的第一个地址

    try:
        order = Order()  # 实例化一个Order 对象
        order.user = L  # 具体用户
        order.orderNo = str(ret)  # 订单编号
        order.adress = A  # 收货地址
        order.acount = float(price * number)  # 商品总价
        order.orderstatus = str("未支付")  # 订单状态

        order.save()
    except BaseException:
        HttpResponse("购买失败")
    else:
        return HttpResponse("ok")


"""确认收货"""
def querenshouhuo(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("不能确认收货")
    if not token:
        return HttpResponse("您未登录")

    id = request.POST.get("id")  # 获取订单的id
    O=Order.objects.filter(id=id).first()#获取该订单
    print(O.goods.id,7777777777777)
    G=Goods.objects.filter(id=O.goods.id).first()#获取该商品
    print(G,99999999999999999)
    L=Login.objects.filter(id=G.user.id).first()#获取卖家用户
    B=Balance.objects.filter(user=L).first()
    print(L.username,00000000000000000)
    with transaction.atomic():  # 禁止自动提交,保证该函数中的所有数据库操作在同一个事物中，第一个数据库操作1即使成功保存到数据库中，只要第2个数据操作失败，那么所有该段代码所有设计的都会更改回滚到原来
        sid = transaction.savepoint()  # 开启事务设置事务保存点
        try:

            Order.objects.filter(id=id).update(orderstatus="已收货")

            Balance.add_amount(B, G.price)  # 订单生成成功，余额减少

        except:
            transaction.savepoint_rollback(sid)  # 失败回滚事务(如果数据库操作发生异常，回滚到设置的事务保存点)
            return HttpResponse("收货失败")
        else:
            transaction.savepoint_commit(sid)  # 如果没有异常，成功提交事物
            return HttpResponse("收货成功")


"""确认收货"""
def delete_order(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:
        return HttpResponse("不能确认收货")
    if not token:
        return HttpResponse("您未登录")

    try:
        id = request.POST.get("id")  # 获取订单的id
        Order.objects.filter(id=id).delete()#获取该订单
    except:
        return HttpResponse("删除失败")
    else:
        return HttpResponse("删除成功")

"""用于用户退出登录"""


def quit(request):
    try:  # 试一试，token=request.session['token']
        token = request.session['token']
        username = request.session['username']
    except:  # 如果出现错误
        return HttpResponse("退出登录失败")
    else:  # 如果没出报错
        pass
    finally:  # finally 不论有没有出错，来这里
        try:
            del request.session['username']
            del request.session['token']
        except:
            return HttpResponse("未登录")
        return HttpResponse("退出登录成功")


def all_products(request):
    g = Goods.objects.all()
    context = {'g': g}
    return render(request, "all_products.html", context=context)

def products_types(request,id):
    type=Product_Types.objects.filter(id=id).first()
    g = Goods.objects.filter(type_id=id)
    context = {'g': g,
               "type":type,
               }
    return render(request, "products_types.html", context=context)

def search(request):
    return render(request, "search.html")


def personal_order(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    if request.method == "GET":
        username = request.session.get("username")
        L = Login.objects.filter(username=username).first()
        B = Balance.objects.filter(user=L).first()

        # 未评价订单
        C_wei = Order.objects.filter(user=L).filter(orderstatus="未支付")

        C_yi = Order.objects.filter(user=L).filter(orderstatus="已支付")

        C_qu = Order.objects.filter(user=L).filter(orderstatus="订单取消")

        C_shou = Order.objects.filter(user=L).filter(orderstatus="已收货")

        context = {"C_qu": C_qu, "C_shou":C_shou,
                   "C_wei": C_wei,
                   "C_yi": C_yi,
                   "B": B,
                   "L": L}

        return render(request, "personal_order.html", context=context)


def base(request):
    return render(request, "base_center.html")


"""个人中心主页"""


def personal_index(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()
    B = Balance.objects.filter(user=L).first()

    context = {"L": L, "B": B}
    return render(request, "personal_index.html", context=context)


def personal_address(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    B = Balance.objects.filter(user=L).first()

    if request.method == "GET":
        address = Adress.objects.filter(user=L)
        return render(request, "personal_address.html",
                      context={"address": address, "L": L, "B": B})

    elif request.method == "POST":
        print(1111111111111111111)
        diqu = request.POST.get("city")
        xiangxidizi = request.POST.get("xiangxidizi")
        name = request.POST.get("name")
        youbian = request.POST.get("youbian")
        phone = request.POST.get("phone")

        try:
            a = Adress()
            a.user = L
            a.receiver_name = name
            a.area = diqu
            a.postcode = int(youbian)
            a.ads = xiangxidizi
            a.phone = phone
            a.save()
        except:
            return HttpResponse("保存失败")
        else:
            return HttpResponse("添加地址成功")


def personal_shoucang(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    f = Favorite.objects.filter(user=L)

    context = {"f": f}
    return render(request, "personal_shoucang.html", context=context)


"""ajax请求添加收藏夹"""

def jiashoucang(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")
    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()
    id = request.POST.get("id")
    G = Goods.objects.filter(id=id).first()

    if Favorite.objects.filter(user=L, goods=G).first():
        Favorite.objects.filter(user=L, goods=G).delete()
        print(1)
        return HttpResponse("取消成功")

    else:
        Favorite.objects.update_or_create(user=L, goods=G)
        print(2)
        return HttpResponse("加入收藏成功")




def personal_comment(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    B = Balance.objects.filter(user=L).first()

    if request.method == "GET":
        # 未评价订单
        C_wei = Order.objects.filter(user=L).filter(is_comment=False).filter(orderstatus="已收货")

        # 已评价
        C_yi = Order.objects.filter(user=L).filter(is_comment=True)

        context = {"L": L, "C_wei": C_wei, "C_yi": C_yi, "B": B}
        return render(request, "personal_comment.html", context=context)

    elif request.method == "POST":
        goods_id = request.POST.get("goods")
        G = Goods.objects.filter(id=goods_id).first()
        type = request.POST.get("type")
        data = request.POST.get("data")
        order_id = request.POST.get("order")
        O = Order.objects.filter(id=order_id).first()
        try:
            c = Comment()
            c.username = L
            c.type = type
            c.content = data
            c.goods = G
            c.order = O
            c.save()
        except:
            return HttpResponse("评论失败")
        else:
            Order.objects.filter(id=order_id).update(is_comment=True)
            return HttpResponse("评论成功")


"""查看评论"""
def chakanpinglun(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")
    comment=request.POST.get("id")#获取前端点击查看评论的id
    comment=Comment.objects.filter(order_id=comment).first()

    dic = {}
    dic["type"] = comment.type
    dic["content"] = comment.content
    dic["time"] = comment.time

    return JsonResponse( dic)

"""发布商品函数"""


def personal_post(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    if request.method == "GET":

        username = request.session.get("username")
        L = Login.objects.filter(username=username).first()

        B = Balance.objects.filter(user=L).first()

        context = {"L": L, 'B': B}
        return render(request, "personal_post.html", context=context)

    elif request.method == "POST":

        mingcheng = request.POST.get("mingcheng")
        file = request.FILES.get("file")
        fenlei = request.POST.get("fenlei")
        price = request.POST.get("jiage")
        miaoshu = request.POST.get("miaoshu")
        data = request.POST.get("data")
        danwei = request.POST.get("danwei")
        kucun = request.POST.get("kucun")
        baoyou = request.POST.get("baoyou")
        youfei = request.POST.get("youfei")
        tuihuan = request.POST.get("tuihuan")

        username = request.session.get("username")
        L = Login.objects.filter(username=username).first()

        try:
            g = Goods()
            g.user = L
            g.title = mingcheng
            g.price = price
            g.desc = miaoshu
            g.content = data
            g.unit = danwei
            g.picture = file
            g.type = fenlei
            g.Seven_days_package_Return = tuihuan
            g.Seven_days_package_Return = tuihuan
            g.Free_shipping = baoyou
            g.postage = youfei
            g.quantity = kucun
            g.save()
        except:
            return HttpResponse("发布失败")
        return HttpResponse("发布成功")


def pay(request):
    if request.method=="POST":
        try:
            token = request.session.get("token")
            token = Token.objects.filter(token=token).first()

        except:  # ret=request.session.get("username") 报错了
            return HttpResponse("未知错误")
        if not token:
            return HttpResponse("您未登录")

        username = request.session.get("username")
        L = Login.objects.filter(username=username).first()

        goods = request.POST.getlist("goods", None)
        if not goods:
            pass
        else:
            goods=[]
            goods.append(request.POST.get("goods"))

        number = (request.POST.get("num"))  # 获取商品的数量

        list_num=[]
        try:
            for i in number.split(","):
                list_num.append(i)
        except:
            list_num = [1,]

        list = []

        list_price=0
        list_yunfei=0
        list_youhui=0

        for i,j in zip(goods,list_num):

            G = Goods.objects.filter(id=int(i)).first()
            time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            ret = time + str(username[0:3])  # 随机生成一个1000到9999的int类型的数
            A = Adress.objects.filter(user=L).first()  # 获取该用户默认的第一个地址

            try:
                order = Order()  # 实例化一个Order 对象
                order.user = L  # 具体用户
                order.goods = G  # 具体商品
                order.orderNo = str(ret)  # 订单编号
                order.adress = A  # 收货地址
                order.acot = int(j)  # 商品数量
                order.acount = float(G.price * int(j))  # 商品总价

                list_price =list_price+ float(G.price * int(j))  # 商品总价传给前端

                list_yunfei =list_yunfei+ G.postage   # 商品总价传给前端

                order.orderstatus = str("未支付")  # 订单状态
                order.save()
            except:
                return HttpResponse("下单失败")

            list.append(order)
        username = request.session.get("username")
        L = Login.objects.filter(username=username).first()
        A = Adress.objects.filter(user=L)
        context = {"L": L, "A": A, "list": list,
                   "list_yunfei":list_yunfei,"list_price":list_price
                   }
        return render(request, "pay.html", context=context)



def ok(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误，不能加入购物车")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")  # 获取浏览器中session里面的username
    L = Login.objects.filter(username=username).first()

    add=request.POST.get("add")

    A=Adress.objects.filter(id=add).first()


    B = Balance.objects.filter(user=L).first()

    order_id = request.POST.getlist("order_id")  # 获取订单的id

    print(order_id)
    try:
        for i in order_id:

            O=Order.objects.filter(id=int(i)).first()
            with transaction.atomic():  # 禁止自动提交,保证该函数中的所有数据库操作在同一个事物中，第一个数据库操作1即使成功保存到数据库中，只要第2个数据操作失败，那么所有该段代码所有设计的都会更改回滚到原来
                sid = transaction.savepoint()  # 开启事务设置事务保存点
                try:

                    if B.amount-O.goods.price<0:
                        raise 707
                    Order.objects.filter(id=int(i)).update(orderstatus="已支付",adress=A)

                    Balance.Less_amount(B, O.goods.price)  # 订单生成成功，余额减少

                except:
                    transaction.savepoint_rollback(sid)  # 失败回滚事务(如果数据库操作发生异常，回滚到设置的事务保存点)
                    return HttpResponse("余额不足")
                else:
                    transaction.savepoint_commit(sid)  # 如果没有异常，成功提交事物

    except BaseException:
        return HttpResponse("购买失败")
    else:
        return render(request, "ok.html")


"""账户安全"""


def personal_account(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    B = Balance.objects.filter(user=L).first()

    context = {"L": L, 'B': B}
    return render(request, "personal_account.html", context=context)


"""个人信息"""


def personal_info(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    B = Balance.objects.filter(user=L).first()

    context = {"L": L, 'B': B}
    return render(request, "personal_info.html", context=context)


"""重置支付密码"""


def personal_resetPay(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    B = Balance.objects.filter(user=L).first()

    context = {"L": L, 'B': B}
    return render(request, "personal_resetPay.html", context=context)


"""重置登录密码"""


def personal_login_pass(request):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    B = Balance.objects.filter(user=L).first()

    context = {"L": L, 'B': B}
    return render(request, "personal_login_pass.html", context=context)


"""重置登录密码"""


def wuliu(request, order_id):
    try:
        token = request.session.get("token")
        token = Token.objects.filter(token=token).first()

    except:  # ret=request.session.get("username") 报错了
        return HttpResponse("未知错误")
    if not token:
        return HttpResponse("您未登录")

    username = request.session.get("username")
    L = Login.objects.filter(username=username).first()

    B = Balance.objects.filter(user=L).first()

    context = {"L": L, 'B': B}
    return render(request, "wuliu.html", context=context)
