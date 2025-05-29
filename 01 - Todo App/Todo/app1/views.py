from django.shortcuts import render
from django.http import  HttpResponse
from .models import Todo
from .forms import *

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    # return HttpResponse("This is Home Page !")
    return render(request, "home.html", context={"todos": todos})

def detail(request, id):
    todo_data = Todo.objects.get(id=id)
    return render(request, "detail.html", context={"data": todo_data})

def create(request):
    # check for post method
    # if it was post then we check it
    if request.method == "POST":
        pass
    # otherwise its get so we show the page
    else:
        form = CreateNoteForm()
    return render(request, "create.html", context={"form": form})