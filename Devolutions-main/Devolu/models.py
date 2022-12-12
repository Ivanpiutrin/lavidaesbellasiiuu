from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.

class Cliente (models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nomproduct = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    costo = models.PositiveIntegerField()

class Devolucion(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Distribuidor = models.CharField(max_length=100)
    fecha = models.DateField()
    nombre_vendedor = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)




