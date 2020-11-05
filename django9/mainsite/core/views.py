from django.shortcuts import render
from .models import Student


def data(request):
    return render(request, 'core/index.html', {'st': Student})
