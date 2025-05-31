from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def user_register(request):
    if request.method == "POST":
        pass
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {"form": form})