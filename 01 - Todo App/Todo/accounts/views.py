from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages

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