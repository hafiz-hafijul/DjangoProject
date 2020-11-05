from django.shortcuts import render
from .forms import StudentRegistration


def showdata(request):
    fm = StudentRegistration()
    return render(request, 'core/registration.html',{'form':fm})