from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def blog(request):
    return render(request, 'main/blog.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def testimonials(request):
    return render(request, 'main/testimonials.html')


def tutorials(request):
    return render(request, 'main/tutorials.html')
