from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from shopapp.models import Goods,Category,Goods_img,Color,Size
from shopapp.utils import function


def item_category(request):
    goods_list=Goods.objects.all()

    # where = function.getWhere(request)
    # goods_num = Goods.objects.filter(**where).all().count()  # 显示记录数
    # goods_list = Goods.objects.filter(**where).all()


    currentPage = int(request.GET.get('page', 1))  # 获取当前在第几页
    paginator = Paginator(goods_list, 5)  # 使用的是文章记录对象,不是art_num
    if paginator.num_pages > 11:
        if currentPage - 5 < 1:
            pageRange = range(1, 11)
        elif currentPage + 5 > paginator.num_pages:
            pageRange = range(currentPage - 5, paginator.num_pages + 1)
        else:
            pageRange = range(currentPage - 5, currentPage + 5)
    else:
        pageRange = range(1, paginator.num_pages + 1)

    #print(pageRange)

    try:
        goods_list = paginator.page(currentPage)
    except PageNotAnInteger:
        goods_list = paginator.page(1)
    except EmptyPage:
        goods_list = paginator.page(paginator.num_pages)


    category1=Category.objects.filter(category_pid_id=None).all()
    category2=Category.objects.filter(category_pid_id=1).all()
    cate_color=Color.objects.all()
    cate_size=Size.objects.all()



    return render(request, 'category/item_category.html',locals())