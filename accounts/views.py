from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        sign_up_form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': sign_up_form})
    elif request.method == 'POST':
        sign_up_form = SignupForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            return redirect('/')
        return render(request, 'accounts/signup.html', {'form': sign_up_form})


def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        sign_in_form = SigninForm()
        return render(request, 'accounts/signin.html', {'form': sign_in_form})
    elif request.method == 'POST':
        sign_in_form = SigninForm(request, request.POST)
        if sign_in_form.is_valid():
            auth.login(request, sign_in_form.get_user())
            return redirect('/')
        return render(request, 'accounts/signup.html', {'form': sign_in_form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')