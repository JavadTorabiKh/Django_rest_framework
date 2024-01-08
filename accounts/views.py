from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    next = request.GET.get('redirect_to')
    if request.user.is_authenticated:
        return redirect('home:home_page')
    login_form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username_input = login_form.cleaned_data.get('username')
            password_input = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                login(request, user)
                if next:
                    return redirect(next)
                else:
                    return redirect('home:home_page')
            else:
                login_form.add_error('password', 'Your username or password is invalid')
    context = {'login_form': login_form}
    return render(request, 'accounts/user_login_page.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')
    register_form = UserRegisterForm()
    if request.method == 'POST':
        register_form = UserRegisterForm(data=request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            password_2 = register_form.cleaned_data.get('password_2')
            user = User.objects.create_user(username=username, password=password_2)
            user.first_name = first_name
            user.email = email
            user.last_name = last_name
            user.save()
            return redirect('accounts:user_login')
    context = {'register_form': register_form}
    return render(request, 'accounts/user_register_page..html', context)


def log_out(request):
    logout(request)
    return redirect('home:home_page')