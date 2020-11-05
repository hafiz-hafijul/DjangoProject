from django.shortcuts import render


def base(request):

    return render(request, 'blog/home.html')


def func(request, my_id):
    id = my_id
    return render(request, 'blog/index.html', {'num':id})