from django.contrib import admin
from django.urls import path, include

from AppGym.views import show_home

urlpatterns = [
    path('inicio/', show_home)
]
