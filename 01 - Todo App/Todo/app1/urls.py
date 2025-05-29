from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("detail/<int:id>", detail, name="details"),
    path("create/", create, name = "create"),
    path("update/<int:id>", update, name="update"),
    path("middle_update/", middle_update, name="middle_update")
]