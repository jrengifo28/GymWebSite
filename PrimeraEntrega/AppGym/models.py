from tabnanny import verbose
from django.db import models

# Create your models here.


class Cliente(models.Model):
    class Meta:
        verbose_name_plural = "Clientes"

    codigo = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    phone = models.IntegerField()
    direccion = models.CharField(max_length=60)
    cumple = models.DateField(null=True)

    def __str__(self):
        return f"({self.codigo}) {self.nombre} {self.apellido}"


class Entrenador(models.Model):
    class Meta:
        verbose_name_plural = "Entrenadores"

    codigo = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    phone = models.IntegerField()
    direccion = models.CharField(max_length=40)
    cumple = models.DateField(null=True)
    profesion = models.CharField(max_length=40)
    tipo_entrenador = models.CharField(max_length=40)

    def __str__(self):
        return f"({self.codigo}) {self.nombre} {self.apellido} - {self.tipo_entrenador}"


class Rutina(models.Model):
    class Meta:
        verbose_name_plural = "Rutinas"

    codigo = models.IntegerField()
    tipo = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    rutina = models.CharField(max_length=1000)

    def __str__(self):
        return f"({self.codigo_rutina}) {self.tipo_rutina} - {self.ubicacion}"
