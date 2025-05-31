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

def update(request, id):
    todo_data = Todo.objects.get(id=id)
    if request.method == "POST":
        form = UpdateNoteForm(request.POST, instance=todo_data)
        if form.is_valid():
            form.save()
            # extra tag is for our bootsrap that show us a good message in green background
            messages.success(request, "Data Updated Successfully !", "success")
            return redirect("home")
    else:
        # for showing the data related to the special record we use instance in forms
        # so that data will be shown on the html template that we have.
        form = UpdateNoteForm(instance=todo_data)
    return render(request, "update.html", context={"form": form})


def middle_update(request):
    """
    information of creation :

    this function is just a middle man that takes the id for a Todo record
    and then send it to the main update url and its related function to work
    and the main part is in update function
    i add this part to use the project easier and i map this middle_update
    to the same name in my navbar.

    """
    if request.method == "POST":
        form = MiddleUpdateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return redirect("update", id=cd["id_"])
    else:
        form = MiddleUpdateForm()
    return render(request, "middle_update.html", {"form": form})

def middle_delete(request):
    if request.method == "POST":
        form = MiddleDeleteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            todo_id = cd["id_"]
            Todo.objects.get(id=todo_id).delete()
            messages.success(request, "Todo Deleted Successfully", "success")
            return redirect("home")

    else:
        form = MiddleDeleteForm()
    return render(request, "middle_delete.html", {"form": form})