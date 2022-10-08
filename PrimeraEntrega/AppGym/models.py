from django.db import models

# Create your models here.


class Cliente(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length="40")
    apellido = models.CharField(max_length="40")
    phone = models.IntegerField()
    direccion = models.CharField(max_length="100")
    cumple = models.DateField()


class Entrenador(models.Model):
    codigo_entrenador = models.IntegerField()
    nombre = models.CharField(max_length="40")
    apellido = models.CharField(max_length="40")
    phone = models.IntegerField()
    direccion = models.CharField(max_length="100")
    cumple = models.DateField()
    profesion = models.CharField(max_length="40")
    tipo_entrenador = models.CharField(max_length="40")


class Rutina(models.Model):
    id = models.IntegerField()
    tipo_rutina = models.CharField(max_length="40")
    ubicacion = models.CharField(max_length="40")
    rutina = models.CharField(max_length="1000")
