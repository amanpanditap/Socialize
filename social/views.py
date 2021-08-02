from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    hello = 'Hello,'
    context = {
        'user': user,
        'hello': hello,
    }
    #return HttpResponse('Hello World')
    return render(request, 'main/home.html', context)