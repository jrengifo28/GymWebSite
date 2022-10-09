from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show_home(request):
    return render(request, "AppGym/inicio.html")

def show_main(request):
    return render(request, "AppGym/main.html")

def procesar_formulario_cliente(request):
    if request.method != "POST":
        return render (request, "AppGym/formularioCliente.html")
    
def procesar_formulario_entrenador(request):
    if request.method != "POST":
        return render (request, "AppGym/formularioEntrenador.html")

def procesar_formulario_rutina(request):
    if request.method != "POST":
        return render (request, "AppGym/formularioRutina.html")