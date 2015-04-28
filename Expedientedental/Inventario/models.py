# -*- encoding: utf-8 -*-
from django.db import models
from decimal import Decimal


class UnidadMedida(models.Model):
        unidad = models.CharField(max_length=15, unique=True)
        prefix = models.CharField(max_length=4)

        def __unicode__(self):
                return '%s %s' % (self.unidad, self.prefix)


class Producto(models.Model):
        producto = models.CharField(max_length=100, unique=True)
        unidad_medida = models.ForeignKey(UnidadMedida)
        porciones = models.DecimalField(max_digits=8, decimal_places=2)
        precio = models.DecimalField(max_digits=8, decimal_places=2)
        descripcion = models.TextField(max_length=120)
        precioUnidad = models.DecimalField(max_digits=8, decimal_places=2,
                                           default=Decimal(u'0.00'))

        def __unicode__(self):
                return u'%s %s %s %s ' % (self.producto, self.unidad_medida,
                                          self.porciones, self.descripcion)

        def in_stock(self):
            """
            Regresa True si esta en stock
            """
            return self.producto.in_stock()

        def get_stock(self):
            """
            Regresa cantidad disponible.
            """
            return self.producto.get_stock()

        def disminuir(self, cantidad_a_quitar, cantidad_a_agregar):
                if self.porciones >= self.cantidad_a_quitar:
                        self.porciones -= cantidad_a_agregar
                        return True
                return False

        def total(self):
                precioUnidad = self.precio/self.porciones
                return '%s' % precioUnidad


class Entradas(models.Model):
        fecha = models.DateTimeField(auto_now=True)
        producto = models.ForeignKey(Producto)
        porciones = models.IntegerField(max_length=5, default=0)

        def get_stock(self):
            return self.producto.get_stock()

        def agregar(self, cantidad_a_agregar):
                self.porciones += cantidad_a_agregar


class Devoluciones(models.Model):
        fecha = models.DateTimeField(auto_now=True)
        producto = models.ForeignKey(Producto)
        cantidad = models.IntegerField(max_length=5, default=0)
        motivo = models.CharField(max_length=100)

        def __unicode__(self):
                return '%s %s %s %s' % (self.producto.producto, self.cantidad,
                                        self.cantidad, self.fecha)
