from django.urls import path, re_path, include
from shopapp.views import index, category, goods_detail, shopcart, user_udai, others

urlpatterns = [


    # index首页路由
    re_path(r'index/', index.index, name='index'),

    # 简单的商品列表页
    re_path(r'item_sale_page/', index.item_sale_page, name='item_sale_page'),




    # category商品列表页路由
    re_path(r'item_category/', category.item_category, name='item_category'),



    # goods_detail商品详情页路由
    re_path(r'item_show/(\d+)/$', goods_detail.item_show, name='item_show'),
    # re_path(r'index/text/(\d+)/$', index.text, name='index/text'),


    # others的路由
    # 网店代购路由开始
    re_path(r'agent_level/', others.agent_level, name='agent_level'),
    # 企业账号
    re_path(r'enterprise_id/', others.enterprise_id, name='enterprise_id'),
    # 网店代购路由结束
    # 网站留言
    re_path(r'issues/', others.issues, name='issues'),
    # 实时下架
    re_path(r'item_remove/', others.item_remove, name='item_remove'),
    # 关于我们网站
    re_path(r'udai_about/', others.udai_about, name='udai_about'),




    # user_udai方法的路由
    # 诚信合约
    re_path(r'udai_contract/', user_udai.udai_contract, name='udai_contract'),
    # 登录路由
    re_path(r'login/', user_udai.login, name='login'),
    re_path(r'enroll/', user_udai.enroll, name='enroll'),

    re_path(r'udai_article/', user_udai.udai_article, name='udai_article'),
    # 物流查询
    re_path(r'udai_mail_query/', user_udai.udai_mail_query, name='udai_mail_query'),
    # 通知消息
    re_path(r'udai_message/', user_udai.udai_message, name='udai_message'),

    re_path(r'udai_modifypay_step1/', user_udai.udai_modifypay_step1, name='udai_modifypay_step1'),
    re_path(r'udai_modifypay_step2/', user_udai.udai_modifypay_step2, name='udai_modifypay_step2'),
    re_path(r'udai_modifypay_step3/', user_udai.udai_modifypay_step3, name='udai_modifypay_step3'),
    re_path(r'udai_modifypwd_step1/', user_udai.udai_modifypwd_step1, name='udai_modifypwd_step1'),
    re_path(r'udai_modifypwd_step2/', user_udai.udai_modifypwd_step2, name='udai_modifypwd_step2'),
    re_path(r'udai_modifypwd_step3/', user_udai.udai_modifypwd_step3, name='udai_modifypwd_step3'),
    re_path(r'udai_notice/', user_udai.udai_notice, name='udai_notice'),
    # 修改支付密码
    re_path(r'udai_paypwd_modify/', user_udai.udai_paypwd_modify, name='udai_paypwd_modify'),
    # 修改登录密码
    re_path(r'udai_pwd_modify/', user_udai.udai_pwd_modify, name='udai_pwd_modify'),

    # 个人资料
    re_path(r'udai_setting/', user_udai.udai_setting, name='udai_setting'),
    # 资金管理
    re_path(r'udai_treasurer/', user_udai.udai_treasurer, name='udai_treasurer'),
    re_path(r'udai_article1/', user_udai.udai_article1, name='udai_article1'),
    re_path(r'udai_article2/', user_udai.udai_article2, name='udai_article2'),
    re_path(r'udai_article3/', user_udai.udai_article3, name='udai_article3'),
    re_path(r'udai_article4/', user_udai.udai_article4, name='udai_article4'),

    # 新手上路
    re_path(r'udai_article5/', user_udai.udai_article5, name='udai_article5'),
    re_path(r'udai_article6/', user_udai.udai_article6, name='udai_article6'),
    re_path(r'udai_article7/', user_udai.udai_article7, name='udai_article7'),
    re_path(r'udai_article8/', user_udai.udai_article8, name='udai_article8'),

    # 网站介绍
    re_path(r'udai_article10/', user_udai.udai_article10, name='udai_article10'),
    re_path(r'udai_article11/', user_udai.udai_article11, name='udai_article11'),
    re_path(r'udai_article12/', user_udai.udai_article12, name='udai_article12'),



    # shopcart方法的路由
    # 商品评价
    re_path(r'order_evaluate/', shopcart.order_evaluate, name='order_evaluate'),
    # 退款/退货
    re_path(r'udai_apply_return/', shopcart.udai_apply_return, name='udai_apply_return'),
    # 我的收藏
    re_path(r'udai_collection/', shopcart.udai_collection, name='udai_collection'),

    # 我的订单
    re_path(r'udai_order/', shopcart.udai_order, name='udai_order'),
    # 订单详情
    re_path(r'udai_order_detail/', shopcart.udai_order_detail, name='udai_order_detail'),

    # 收货地址
    re_path(r'udai_address/', shopcart.udai_address, name='udai_address'),
    # 修改收货地址
    re_path(r'udai_address_edit/', shopcart.udai_address_edit, name='udai_address_edit'),

    # 确认收货
    re_path(r'udai_order_receipted/', shopcart.udai_order_receipted, name='udai_order_receipted'),

    # 退款/退货
    re_path(r'udai_refund/', shopcart.udai_refund, name='udai_refund'),
    # 我的购物车
    re_path(r'udai_shopcart/', shopcart.udai_shopcart, name='udai_shopcart'),
    re_path(r'udai_shopcart_pay/', shopcart.udai_shopcart_pay, name='udai_shopcart_pay'),

    # 我的U袋也是用户中心
    re_path(r'udai_welcome/', shopcart.udai_welcome, name='udai_welcome'),

]
