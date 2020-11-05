from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registration
from .models import User
# Create your views here.
def thank(request):
    return render(request, 'blog/success.html')



def showdata(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            regi = User(name=nm, email=em, password=pw)
            regi.save()
            return HttpResponseRedirect('/regi/success/' )
    else:
        fm = Registration()
    return render(request, 'blog/home.html', {'form':fm})