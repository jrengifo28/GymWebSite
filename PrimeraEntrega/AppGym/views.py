from django.http import HttpResponse
from django.shortcuts import render
from AppGym.models import Cliente, Entrenador, Rutina
from AppGym.forms import ClientesForm, EntrenadoresForm, RutinasForm

# Create your views here.


def inicio(request):
    return render(request, "AppGym/inicio.html")


def procesar_formulario_cliente(request):
    if request.method == "GET":
        mi_formulario = ClientesForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "AppGym/formularioCliente.html", context=contexto)

    if request.method == "POST":
        mi_formulario = ClientesForm(request.POST)
        if mi_formulario.is_valid():
            datos_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Cliente(
                codigo=datos_usuario["codigo"],
                nombre=datos_usuario["nombre"],
                apellido=datos_usuario["apellido"],
                phone=datos_usuario["phone"],
                direccion=datos_usuario["direccion"],
                cumple=datos_usuario["cumple"],
            )
            nuevo_modelo.save()

            return render(request, "AppGym/formularioCliente.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "AppGym/formularioCliente.html", context=contexto)


def procesar_formulario_entrenador(request):
    if request.method == "GET":
        mi_formulario = EntrenadoresForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "AppGym/formularioEntrenador.html", context=contexto)

    if request.method == "POST":
        mi_formulario = EntrenadoresForm(request.POST)
        if mi_formulario.is_valid():
            datos_entrenador = mi_formulario.cleaned_data
            nuevo_modelo = Entrenador(
                codigo=datos_entrenador["codigo"],
                nombre=datos_entrenador["nombre"],
                apellido=datos_entrenador["apellido"],
                phone=datos_entrenador["phone"],
                direccion=datos_entrenador["direccion"],
                cumple=datos_entrenador["cumple"],
                profesion=datos_entrenador["profesion"],
                tipo_entrenador=datos_entrenador["tipo de entrenador"],
            )
            nuevo_modelo.save()

            return render(request, "AppGym/formularioEntrenador.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "AppGym/formularioEntrenador.html", context=contexto)


def procesar_formulario_rutina(request):
    if request.method == "GET":
        mi_formulario = RutinasForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "AppGym/formularioRutina.html", context=contexto)

    if request.method == "POST":
        mi_formulario = RutinasForm(request.POST)
        if mi_formulario.is_valid():
            datos_rutina = mi_formulario.cleaned_data
            nuevo_modelo = Rutina(
                codigo=datos_rutina["codigo"],
                estilo_rutina=datos_rutina["estilo de rutina"],
                ubicacion=datos_rutina["ubicacion"],
                rutina=datos_rutina["rutina"],
            )
            nuevo_modelo.save()

            return render(request, "AppGym/formularioRutina.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "AppGym/formularioRutina.html", context=contexto)


def buscar_cliente(request):
    if request.method == "GET":
        return render(request, "AppGym/busquedaCliente.html")

    if request.method == "POST":
        nombre_a_buscar = request.POST["nombre"]
        resultado_busqueda = Cliente.objects.filter(nombre=nombre_a_buscar)
        contexto = {"resultados": resultado_busqueda}
        return render(request, "AppGym/resultadoCliente.html", context=contexto)
