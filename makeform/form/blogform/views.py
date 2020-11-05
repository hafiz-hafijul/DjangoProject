from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration


def thank(request):
    return render(request, 'form/success.html',)



def showdataform(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            return HttpResponseRedirect('/regi/success/')

    else:
        fm = StudentRegistration()
    return render(request,'form/registration.html', {'form':fm})