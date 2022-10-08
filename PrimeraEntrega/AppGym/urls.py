from django.contrib import admin
from django.urls import path, include

from AppGym.views import show_home, show_main

urlpatterns = [
    path('main/', show_main),
    path('inicio/', show_home)
]
