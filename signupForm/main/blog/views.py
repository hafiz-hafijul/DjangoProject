from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# signup function


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Your Signup Successfully !!!')
        else:
            fm = SignUpForm()
        return render(request, 'blog/signup.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


# profile function


def user_profile(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/profile.html')
    else:
        return HttpResponseRedirect('/login/')

# login function


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                return HttpResponseRedirect('/profile/')
                messages.success(request, 'Your Logging Successfully !!!')
        else:
            fm = AuthenticationForm()
        return render(request, 'blog/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


# logout function


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
