# -*- encoding: utf-8 -*-

from django.db import models
from decimal import Decimal
from django.contrib import admin





class UnidadMedida(models.Model):
        unidad = models.CharField(max_length=15)
        prefix = models.CharField(max_length=4)

        def __unicode__(self):
                return '%s %s'%(self.unidad,self.prefix)



class Producto(models.Model):        
        producto      = models.CharField(max_length=100)
        unidad_medida = models.ForeignKey(UnidadMedida)
        porciones     = models.DecimalField(max_digits=8,decimal_places=2)
        precio        = models.DecimalField(max_digits = 8, decimal_places = 2)
        descripcion   = models.TextField(max_length=120)
        precioUnidad  = models.DecimalField(max_digits = 8, decimal_places = 2,default=Decimal(u'0.00'))
        
        def __unicode__(self): 
                return '%s %s %s %s '%(self.producto,self.unidad_medida,self.porciones,self.descripcion)

        def total(self):
                precioUnidad =self.precio/self.porciones
                return '%s'% precioUnidad 


class Entradas(models.Model):
        fecha = models.DateTimeField(auto_now=True)
        producto = models.ForeignKey(Producto)
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






                


