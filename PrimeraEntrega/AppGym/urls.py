from django.contrib import admin
from django.urls import path, include

from AppGym.views import (
    show_home,
    show_main,
    buscar_cliente,
    procesar_formulario_cliente,
    procesar_formulario_entrenador,
    procesar_formulario_rutina,
)

urlpatterns = [
    path("main/", show_main),
    path("inicio/", show_home),
    path("buscarCliente/",buscar_cliente),
    path("formularioCliente/", procesar_formulario_cliente),
    path("formularioEntrenador/", procesar_formulario_entrenador),
    path("formularioRutina/", procesar_formulario_rutina),
]
