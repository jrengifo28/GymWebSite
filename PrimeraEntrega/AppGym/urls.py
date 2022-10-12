from django.contrib import admin
from django.urls import path

from AppGym.views import (
    inicio,
    buscar_cliente,
    procesar_formulario_cliente,
    procesar_formulario_entrenador,
    procesar_formulario_rutina,
)

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("formularioCliente/", procesar_formulario_cliente, name="Cliente"),
    path("formularioEntrenador/", procesar_formulario_entrenador, name="Entrenador"),
    path("formularioRutina/", procesar_formulario_rutina, name="Rutina"),
    path("busquedaCliente/", buscar_cliente, name="Buscar Cliente"),
    path("resultadoCliente/", buscar_cliente, name="Resultado Cliente"),
]
