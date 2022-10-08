from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def show_main(request):
    return render(request, "AppGym/main.html")


def show_home(request):
    return render(request, "AppGym/inicio.html")
