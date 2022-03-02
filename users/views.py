from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .models import *
from .forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        
    context = {'form' : form}
    return render(request, 'users/register.html', context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/noteapp/')
        else:
            messages.error(request, 'Wrong password or login')


    context = {}
    
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login')
