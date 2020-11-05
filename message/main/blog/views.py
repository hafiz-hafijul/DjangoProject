from django.shortcuts import render
from django.contrib import messages
from .form import StudentData
from .models import User


# Create your views here.

def home(requset):
    if requset.method == 'POST':
        fm = StudentData(requset.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            regi = User(name=nm, email=em, password=pw)
            regi.save()
            messages.success(requset, 'Your login Successful !!!')
    else:
        fm = StudentData()
    return render(requset, 'blog/home.html', {'form':fm})