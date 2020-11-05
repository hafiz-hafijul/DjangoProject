from django.shortcuts import render
from django.contrib import messages
from .forms import ShowData
from .models import User

# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = ShowData(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            regi= User(name=nm, email=em, password=pw)
            regi.save()
            messages.success(request, 'Your Login Success !!!')
    else:
        fm= ShowData()
    return render(request, 'blog/home.html', {'form':fm})