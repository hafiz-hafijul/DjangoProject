from django.shortcuts import render, HttpResponseRedirect
from .forms import Registration
from .models import User


# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = Registration()
    else:
        fm = Registration()
    # data redrive
    stud = User.objects.all()
    # end_data redrive
    return render(request, 'blog/home.html', {'form': fm, 'stu': stud})


def edup(request, id):
    if request.method == 'POST':
        dt = User.objects.get(pk=id)
        fm = Registration(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
    else:
        dt = User.objects.get(pk=id)
        fm = Registration(instance=dt)
    return render(request, 'blog/edup.html', {'form': fm})


def delete(request, id):
    if request.method == 'POST':
        de = User.objects.get(pk=id)
        de.delete()
    return HttpResponseRedirect('/')
