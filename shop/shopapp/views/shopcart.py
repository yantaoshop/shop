from django.shortcuts import HttpResponse,render,redirect

def order_evaluate(request):
    return render(request, 'shopcart/order_evaluate.html')
def udai_address(request):
    return render(request, 'user_udai/udai_address.html')
def udai_address_edit(request):
    return render(request, 'user_udai/udai_address_edit.html')
def udai_apply_return(request):
    return render(request, 'shopcart/udai_apply_return.html')
def udai_order(request):
    return render(request, 'shopcart/udai_order.html')
def udai_order_detail(request):
    return render(request, 'shopcart/udai_order_detail.html')
def udai_order_receipted(request):
    return render(request, 'shopcart/udai_order_receipted.html')
def udai_collection(request):
    return render(request, 'shopcart/udai_collection.html')
def udai_refund(request):
    return render(request, 'shopcart/udai_refund.html')
def udai_shopcart_pay(request):
    return render(request, 'shopcart/udai_shopcart_pay.html')
def udai_shopcart(request):
    return render(request, 'shopcart/udai_shopcart.html')
def udai_welcome(request):
    return render(request, 'shopcart/udai_welcome.html')
