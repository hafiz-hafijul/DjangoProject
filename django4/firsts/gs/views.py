from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request): 
    return render(request,'generator/home.html')


def password(request):
    charecters = list('abcdefghijklmnopqrstuvwxyz')

    if request.Get.get('uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
)

    
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charecters)


    return render(request,'generator/password.html',{'password':thepassword})