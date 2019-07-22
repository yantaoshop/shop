from django.db import models

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=32)
    user_pwd=models.CharField(max_length=120)
    user_tel=models.CharField(max_length=11,null=True)
    user_extra_money=models.IntegerField(null=True,default=0)
    user_paypwd=models.IntegerField(null=True)

class Address(models.Model):
    address_id=models.AutoField(primary_key=True)
    address_province=models.CharField(verbose_name='省份',max_length=32)
    address_city=models.CharField(verbose_name='市',max_length=32)
    address_area=models.CharField(verbose_name='区',max_length=32,null=True)
    address_definite=models.CharField(verbose_name='详细地址',max_length=120)
    address_name=models.CharField(verbose_name='收件人',max_length=32)
    address_tel=models.CharField(verbose_name='收件人号码',max_length=11)
    #一个用户可以有多个收货地址
    address_default=models.IntegerField(default=0,null=True)  #1,表示默认收件地址,已勾选   0,表示普通地址
    user=models.ForeignKey(to='User',on_delete=models.CASCADE)


class Order(models.Model):
    """
    订单表
    """
    order_id=models.AutoField(primary_key=True)       #4：已收货   5：已完成
    order_status=models.IntegerField()      #订单状态：1，未支付  2，已支付未发货   3，已发货待收货
    order_pay_way=models.IntegerField()     #支付方法：1，余额支付 2，微信支付  3，支付宝  4，银行卡支付
    order_addtime=models.DateTimeField()
    order_number=models.CharField(max_length=60)    #订单号
    order_address_province = models.CharField(verbose_name='省份', max_length=32)
    order_address_city = models.CharField(verbose_name='市', max_length=32)
    order_address_area = models.CharField(verbose_name='区', max_length=32, null=True)
    order_address_definite = models.CharField(verbose_name='详细地址', max_length=120)
    order_address_name = models.CharField(verbose_name='收件人', max_length=32)
    order_address_tel = models.CharField(verbose_name='收件人号码', max_length=11)
    #用户id
    user=models.ForeignKey(to='User',on_delete=models.CASCADE)
    #地址id
    address=models.ForeignKey(to='Address',on_delete=models.CASCADE)

#首页/列表页分类：一级、二级、三级分类
class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(verbose_name='类名',max_length=32)
    #关联本表id
    category_pid=models.ForeignKey(verbose_name='关联分类id',to='Category',null=True,related_name='parents',help_text='父id',
                                   on_delete=models.CASCADE)


#商品详情页
class Goods(models.Model):
    goods_id=models.AutoField(primary_key=True)
    goods_name=models.CharField(verbose_name='商品名称',max_length=200)
    goods_original_price=models.FloatField(verbose_name='商品原价',null=True)
    goods_current_price=models.FloatField(verbose_name='商品现价',null=True)
    goods_month_saled=models.IntegerField(verbose_name='月销量',null=True)
    goods_inventory=models.IntegerField(verbose_name='现存货',null=True)
    goods_addtime=models.DateTimeField(verbose_name='商品上架时间',null=True)
    goods_desc=models.CharField(verbose_name='商品简介',max_length=255)
    goods_content=models.TextField(verbose_name='商品内容',null=True)
    goods_img=models.CharField(verbose_name='商品图片',null=True,max_length=120)
    #关联分类id
    category=models.ForeignKey(to='Category',on_delete=models.CASCADE)
    #颜色id
    color=models.ForeignKey(to='Color',on_delete=models.CASCADE)
    #尺码id
    size=models.ForeignKey(to='Size',on_delete=models.CASCADE)



#商品颜色表
class Color(models.Model):
    color_id=models.AutoField(primary_key=True)
    color_name=models.CharField(verbose_name='颜色名',max_length=16)

#商品尺码表
class Size(models.Model):
    size_id=models.AutoField(primary_key=True)
    size_num=models.CharField(verbose_name='尺码大小',max_length=16)


#商品图片路径
class Goods_img(models.Model):
    goods_img_id=models.AutoField(primary_key=True)
    goods_img_path=models.CharField(verbose_name='图片路径',max_length=120)
    #商品id
    goods=models.ForeignKey(to='Goods',on_delete=models.CASCADE,related_name='goods_goods_img')


#购物车
class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    cart_num=models.IntegerField(verbose_name='商品数量',default=0,null=True)
    #商品id
    goods=models.ForeignKey(to='Goods',on_delete=models.CASCADE)
    #用户id
    user=models.ForeignKey(to='User',on_delete=models.CASCADE)


#订单详情
class Order_detail(models.Model):
    order_detail_id=models.AutoField(primary_key=True)
    #商品id
    goods=models.ForeignKey(to='Goods',on_delete=models.CASCADE)
    #订单id：   订单中可以有多个商品
    order=models.ForeignKey(to='Order',on_delete=models.CASCADE)

    order_goods_name=models.CharField(verbose_name='订单商品名称',max_length=72)
    order_goods_price=models.FloatField(verbose_name='订单商品价格',null=True)
    order_goods_num=models.IntegerField(verbose_name='商品数量',default=0,null=True)
    order_goods_img=models.CharField(verbose_name='图片路径',null=True,max_length=120)
    #与商品详情表颜色尺码不同，这是订单买过之后的状态，从颜色尺码那里传过来的值
    order_goods_color=models.CharField(verbose_name='订单商品颜色',null=True,max_length=16)
    order_goods_size=models.CharField(verbose_name='订单商品尺码',null=True,max_length=16)




#评论表
class Comment(models.Model):
    #
    comment_id=models.AutoField(primary_key=True)
    comment_content=models.TextField(verbose_name='评论内容')
    comment_addtime=models.DateTimeField(verbose_name='评论时间',auto_now_add=True)
    comment_goods_color=models.CharField(verbose_name='评论的商品颜色',null=True,max_length=16)
    comment_goods_size=models.CharField(verbose_name='评论的商品尺码',null=True,max_length=16)
    #用户id
    user=models.ForeignKey(to='User',on_delete=models.CASCADE)
    #商品id    根据商品id 得到所有的评论
    goods=models.ForeignKey(to='Goods',on_delete=models.CASCADE)






















