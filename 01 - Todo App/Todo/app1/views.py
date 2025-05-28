from django.shortcuts import render
from django.http import  HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    # return HttpResponse("This is Home Page !")
    return render(request, "home.html", context={"todos": todos})