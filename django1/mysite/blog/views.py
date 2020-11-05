from django.shortcuts import render


def home(request):
    return render(request, 'blog/index.html')


def identity(request, name):
    return render(request, 'blog/index.html')


def single_page(request, id):
    return render(request, 'blog/index.html')
