from django.db import models

# Create your models here.
class riesgoso(models.Model):
    nombre = models.CharField(max_length=20,)
    afeccion = models.CharField(max_length=20,)
    fecha_de_ingreso = models.DateField()

class inofensivo(models.Model):
        nombre = models.CharField(max_length=20,)
        afeccion = models.CharField(max_length=20,)
        fecha_de_ingreso = models.DateField()

class potencial_riesgo(models.Model):
        nombre = models.CharField(max_length=20,)
        afeccion = models.CharField(max_length=20,)
        fecha_de_ingreso = models.DateField()

class curados(models.Model):
        nombre = models.CharField(max_length=20,)
        afeccion = models.CharField(max_length=20,)
        fecha_de_ingreso = models.DateField()
        fecha_de_egreso = models.DateField()

class dados_de_baja(models.Model):
        nombre = models.CharField(max_length=20,)
        afeccion = models.CharField(max_length=20,)
        fecha_de_ingreso = models.DateField()
        fecha_de_egreso = models.DateField()


