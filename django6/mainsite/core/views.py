from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def learn(request):
    return render(request, 'core/django.html')