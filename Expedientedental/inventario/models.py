# -*- encoding: utf-8 -*-
from django.db import models
from decimal import Decimal


class UnidadMedida(models.Model):
        unidad = models.CharField(max_length=15, unique=True)
        prefix = models.CharField(max_length=4)

        def __unicode__(self):
                return '%s ' % (self.prefix)


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
            return self.porciones > 0

        def get_stock(self):
            """
            Regresa cantidad disponible.
            """
            return self.porciones

        def agregar(self, cantidad_a_agregar):
            self.porciones += cantidad_a_agregar

        def total(self):
            precioUnidad = self.precio/self.porciones
            return '%s' % precioUnidad


class Entradas(models.Model):
    '''
    modelo de entrada de cantidad en producto(porciones)
    '''
    fecha = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(Producto)
    porciones = models.IntegerField(max_length=5, default=0)

    def get_stock(self):
            return self.producto.get_stock()

    def agregar(self, cantidad_a_agregar):
            self.porciones += cantidad_a_agregar


class Egresos(models.Model):
    '''
modelo donde se puede corregir un error de captura pero , con un antecedente
    '''
    fecha = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(Producto)
    porciones = models.IntegerField(max_length=5, default=0)
    motivo = models.TextField()

    def __unicode__(self):
        pass

    def egreso_corregir(self):
        existencia = self.producto.porciones - self.porciones
        return existencia


class Devoluciones(models.Model):
    '''
    modelo que permite la devolucion de un insumo
    si y solo si ya se surtio un paquete 
    '''
    fecha = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField(max_length=5, default=0)
    motivo = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s %s %s %s' % (self.producto.producto, self.cantidad,
                                self.cantidad, self.fecha)
