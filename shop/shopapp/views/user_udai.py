from django.shortcuts import HttpResponse,render,redirect

def login(request):
    return render(request, 'user_udai/login.html', locals())

def enroll(request):
    return render(request, 'user_udai/enroll.html', locals())



def udai_article(request):
    return render(request, 'user_udai/udai_article.html')
def udai_contract(request):
    return render(request, 'user_udai/udai_contract.html')
def udai_mail_query(request):
    return render(request, 'user_udai/udai_mail_query.html')
def udai_message(request):
    return render(request, 'user_udai/udai_message.html')
def udai_modifypay_step1(request):
    return render(request, 'user_udai/udai_modifypay_step1.html')
def udai_modifypay_step2(request):
    return render(request, 'user_udai/udai_modifypay_step2.html')
def udai_modifypay_step3(request):
    return render(request, 'user_udai/udai_modifypay_step3.html')
def udai_modifypwd_step1(request):
    return render(request, 'user_udai/udai_modifypwd_step1.html')
def udai_modifypwd_step2(request):
    return render(request, 'user_udai/udai_modifypwd_step2.html')
def udai_modifypwd_step3(request):
    return render(request, 'user_udai/udai_modifypwd_step3.html')
def udai_notice(request):
    return render(request, 'user_udai/udai_notice.html')
def udai_paypwd_modify(request):
    return render(request, 'user_udai/udai_paypwd_modify.html')
def udai_pwd_modify(request):
    return render(request, 'user_udai/udai_pwd_modify.html')
def udai_setting(request):
    return render(request, 'user_udai/udai_setting.html')
def udai_treasurer(request):
    return render(request, 'user_udai/udai_treasurer.html')


def udai_article1(request):
    return render(request,'temp_article/udai_article1.html')
def udai_article2(request):
    return render(request,'temp_article/udai_article2.html')
def udai_article3(request):
    return render(request,'temp_article/udai_article3.html')
def udai_article4(request):
    return render(request,'temp_article/udai_article4.html')
def udai_article5(request):
    return render(request,'temp_article/udai_article5.html')
def udai_article6(request):
    return render(request,'temp_article/udai_article6.html')
def udai_article7(request):
    return render(request,'temp_article/udai_article7.html')
def udai_article8(request):
    return render(request,'temp_article/udai_article8.html')
def udai_article10(request):
    return render(request,'temp_article/udai_article10.html')
def udai_article11(request):
    return render(request,'temp_article/udai_article11.html')
def udai_article12(request):
    return render(request,'temp_article/udai_article12.html')