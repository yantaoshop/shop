from django.shortcuts import HttpResponse,render,redirect

def agent_level(request):
    return render(request, 'others/agent_level.html')


def enterprise_id(request):
    return render(request, 'others/enterprise_id.html')

def issues(request):
    return render(request, 'others/issues.html')
def item_remove(request):
    return render(request, 'others/item_remove.html')

def udai_about(request):
    return render(request, 'others/udai_about.html')