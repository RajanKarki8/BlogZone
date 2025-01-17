from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for',{username})
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
            'form':form
        }
    return render(request, 'auth_user/register.html', context)

def UserLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
           messages.info(request, 'user does not exits')
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in as {user}.')
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'auth_user/login.html', context)

def UserLogout(request):
    logout(request)
    messages.info(request, 'You Have Been logout!')
    return redirect('home')