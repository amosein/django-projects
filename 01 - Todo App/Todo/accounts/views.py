from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"], cd["email"], cd["password"])
            messages.success(request, "User Created Successfully", "success")
            return redirect("home")
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd["username"]
            password = cd["password"]
            # first we validate our user
            user = authenticate(request, username=username, password=password)
            # if it is not valid, it will return None
            if user is not None:
                # here we login our user
                login(request, user)
                messages.success(request, "User Login Successfully !", "success")
                return redirect("home")
            else:
                messages.error(request, "Username and Password is not Match", "danger")


    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    messages.success(request, "User Logout successfully !!", "success")
    return redirect("home")