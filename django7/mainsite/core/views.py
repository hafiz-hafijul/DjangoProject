from django.shortcuts import render



def home(request):
    return render(request, 'core/home.html',{'home':'/home'})

def about(request):
    return render(request, 'core/about.html',{'about':'/about'})

def learn(request):
    return render(request, 'core/django.html',{'learn':'/learn'})