from django.contrib import admin
from django.urls import path, include

from AppGym.views import (
    # show_home,
    show_main,
    buscar_cliente,
    procesar_formulario_cliente,
    procesar_formulario_entrenador,
    procesar_formulario_rutina,
)

urlpatterns = [
    path("main/", show_main, name="Inicio"),
    # path("inicio/", show_home),
    path("formularioCliente/", procesar_formulario_cliente, name="Cliente"),
    path("formularioEntrenador/", procesar_formulario_entrenador, name="Entrenador"),
    path("formularioRutina/", procesar_formulario_rutina, name="Rutina"),
    path("ResultadoCliente/", buscar_cliente, name=" Resultado Cliente"),
    path("BusquedaCliente/", buscar_cliente, name="Buscar Cliente"),
]
