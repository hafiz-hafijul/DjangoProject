from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            regi = User(name=nm, email=em, password=pw)
            regi.save()
    else:
        fm = StudentRegistration()

    return render(request, 'blog/form.html', {'form':fm})