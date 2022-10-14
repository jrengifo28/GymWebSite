from django import forms


class ClientesForm(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    phone = forms.IntegerField()
    direccion = forms.CharField(max_length=60)
    cumple = forms.DateField()


class EntrenadoresForm(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    phone = forms.IntegerField()
    direccion = forms.CharField(max_length=40)
    cumple = forms.DateField()
    profesion = forms.CharField(max_length=40)
    tipo_entrenador = forms.CharField(max_length=40)


class RutinasForm(forms.Form):
    codigo = forms.IntegerField()
    tipo = forms.CharField(max_length=40)
    ubicacion = forms.CharField(max_length=40)
    rutina = forms.CharField(max_length=1000)
