from django.shortcuts import render
import random

def home(request):
    return render(request, 'blog/home.html')

def password(request):
    charecters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.Get.get('length'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(charecters)

        
    return render(request, 'blog/password.html',{'passwords':thepassword})