from django.shortcuts import HttpResponse,render,redirect
from collections import OrderedDict    #对字典对象中元素的排序
from shopapp.models import *


# 首页开始
def index(request):

    # 取出种类表里的一级二级菜单
    category_all = OrderedDict()
    # 找出一级菜单          pid=null
    category_first = Category.objects.filter(category_pid_id__isnull=True).all()
    for v in category_first:  # 遍历一级菜单
        # 得到每一个一级菜单自己下的二级菜单
        category_secend = Category.objects.filter(category_pid_id=v.category_id).all()
        # 拼接二维数组
        category_all[v.category_id] = {
            'id': v.category_id,  # 一级菜单ID
            'name': v.category_name,  # 一级菜单名字
            'children': category_secend  # 自己的子菜单
        }

    # 取出种类表里的二级三级菜单
    category_secend_all = OrderedDict()


    # 遍历一级二级菜单二维数组
    for k,v in category_all.items():
        # print(v)
        # 遍历一级菜单下的子菜单（也就是它下面的二级菜单）
        for i in v["children"]:
            # 取出二级菜单下的三级菜单
            category_third = Category.objects.filter(category_pid_id=i.category_id).all()
            # 在拼接一个二维数组
            category_secend_all[i.category_id] = {
                'id': i.category_id,  # 二级菜单ID
                'name': i.category_name,  # 二级菜单名字
                'children': category_third  # 三级菜单（也就是子菜单）
            }
    # print(category_secend_all)
    # for k,v in category_secend_all.items():
    #     print(v)



    # 取出商品表里的全部数据
    goods_all = Goods.objects.all()




    return render(request, 'index/index.html',locals())






def item_sale_page(request):
    return render(request, 'index/item_sale_page.html')