from django.db import models
from decimal import Decimal
from django.contrib import admin

# Realizar views cuando termine Ray

class Categoria(models.Model):
        nombre = models.CharField(max_length=50)
        
        def __unicode__(self):
                return '%s'% (self.nombre)


class Producto(models.Model):
        precio = models.DecimalField(max_digits = 8, decimal_places = 2)
        categoria = models.ForeignKey(Categoria)
        nombre = models.CharField(max_length=60)
        descripcion = models.TextField(max_length=120)

        def __unicode__(self):
                return '%s'% (self.nombre)


class Entradas(models.Model):
        fecha = models.DateTimeField(auto_now=True)
        nombre = models.ForeignKey(Producto)
        cantidad = models.IntegerField(max_length=5, default=0)

        def agregar(self, cantidad_a_agregar):
                self.cantidad += cantidad_a_agregar

        def quitar(self, cantidad_a_quitar):
                if self.cantidad >= self.cantidad_a_quitar:
                        self.cantidad -= cantidad_a_agregar
                        return True
                return False

        def total(self):
                total = self.cantidad * self.nombre.precio
                return '$%s'% total
                

class Detalles(models.Model):
        fecha = models.DateTimeField(auto_now=True)
        producto = models.ForeignKey(Producto)
        cantidad = models.ForeignKey(Entradas)


        def __unicode__(self):
                return '%s %s'% (self.producto.nombre, self.cantidad.cantidad)
