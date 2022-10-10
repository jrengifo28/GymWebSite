from django import forms


class ClienteForm(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    phone = forms.IntegerField()
    direccion = forms.CharField(max_length=60)
    cumple = forms.DateField(null=True)


class EntrenadorForm(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    phone = forms.IntegerField()
    direccion = forms.CharField(max_length=40)
    cumple = forms.DateField(null=True)
    profesion = forms.CharField(max_length=40)
    tipo_entrenador = forms.CharField(max_length=40)


class RutinaForm(forms.Form):
    codigo_rutina = forms.IntegerField()
    tipo_rutina = forms.CharField(max_length=40)
    ubicacion = forms.CharField(max_length=40)
    rutina = forms.CharField(max_length=1000)
