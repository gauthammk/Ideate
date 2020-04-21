from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import ValidationError
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your new account has been created!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form,
                                                   'title': 'Register'})


@login_required
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your new account has been updated!')
            return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/update.html', {'form': form,
                                                 'title': 'Update'})


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(
                    request, 'The username or password you have provided is incorrect.')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form,
                                                'title': 'Login'})


@login_required
def logoutUser(request):
    logout(request)
    return render(request, 'users/logout.html')
