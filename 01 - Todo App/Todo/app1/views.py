from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import Todo
from .forms import *
from django.contrib import messages

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
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            Todo.objects.create(title=clean_data["title"], body=clean_data["body"])
            messages.success(request, "Todo Saved Successfully !", "success")
            return redirect( "home")
    # otherwise its get so we show the page
    else:
        form = CreateNoteForm()
    return render(request, "create.html", context={"form": form})