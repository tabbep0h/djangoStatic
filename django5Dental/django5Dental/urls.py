from django.contrib import admin
from django.urls import path
from django5Dentalapp import views

urlpatterns = [
    path("",views.index)

]
