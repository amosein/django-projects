from django.urls import path
from .views import *

urlpatterns = [
    path("register/", user_register, name="user_register")
]