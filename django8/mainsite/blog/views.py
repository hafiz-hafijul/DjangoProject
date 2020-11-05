from django.shortcuts import render


def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def course(request):
    return render(request,'core/course.html')

def contact(request):
    return render(request,'core/contact.html')