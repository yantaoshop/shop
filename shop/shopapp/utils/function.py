import random
def range_num(num):
    # 定义一个种子，从这里面随机拿出一个值，可以是字母
    seeds = "1234567890"
    # 定义一个空列表，每次循环，将拿到的值，加入列表
    random_num = []
    # choice函数：每次从seeds拿一个值，加入列表
    for i in range(num):
        random_num.append(random.choice(seeds))
    # 将列表里的值，变成四位字符串
    return "" . join(random_num)#5454


def getWhere(request):
    where = dict()
    article_title=request.POST.get('key','')
    article_isrecommend = request.POST.get('article_isrecommend', '')
    username = request.POST.get('username', '')

    if article_title:
        where['article_title__icontains']=article_title
    if article_isrecommend!='':
        where['article_isrecommend'] = article_isrecommend
    if username:
        where['user__user_loginname__icontains'] = username

    # print(where)
    return where

def userWhere(request):     #后台查询用户
    where=dict()
    user_list = request.POST.get('user_list', '')
    if user_list:
        where['user_loginname__icontains'] = user_list
    return where

def mesWhere(request):     #后台查询用户
    where=dict()
    user = request.POST.get('username', '')
    if user:
        where['user__user_loginname__icontains'] = user
    return where

def comWhere(request):     #后台查询用户
    where=dict()
    user_list = request.POST.get('username', '')
    title = request.POST.get('title', '')
    if user_list:
        where['user__user_loginname__icontains'] = user_list
    if title:
        where['article__article_title__icontains']=title
    return where


def rencent_date():
    import datetime
    current=datetime.datetime.now()
    lists=[]
    for i in range(1,8):
        oneday=datetime.timedelta(days=i)
        day=current - oneday
        date_to = datetime.datetime(day.year,day.month,day.day)
        lists.append(str(date_to)[0:10])
    return lists