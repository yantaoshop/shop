from django.shortcuts import HttpResponse,render,redirect

from shopapp.models import *
def item_show(request,id):
    goods_first = Goods.objects.filter(goods_id=id).first()

    # 根据商品ID取出图片表里的所有数据
    img_all = Goods_img.objects.filter(goods_id=id).all()
    # 爆款专区
    goods_hot = Goods.objects.all()
    return render(request, 'goods_detail/item_show.html',locals())