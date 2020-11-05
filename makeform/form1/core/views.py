from django.shortcuts import render
from .forms import StudentRegistration

def showdata(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Name : ', fm.cleaned_data['name'])
            print('Email : ', fm.cleaned_data['email'])
    else:
        fm = StudentRegistration()
    return render(request, 'core/form.html', {'form':fm})