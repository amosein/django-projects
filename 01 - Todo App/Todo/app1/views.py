from django.shortcuts import render
from django.http import  HttpResponse

from University_Project.Test.c6 import total_data
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    # return HttpResponse("This is Home Page !")
    return render(request, "home.html", context={"todos": todos})

def detail(request, id):
    todo_data = Todo.objects.get(id=id)
    return render(request, "detail", context={"data": todo_data})