from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("",FirstPage,name="home"),
    path("second",SecondPage,name="corazon"),
]
