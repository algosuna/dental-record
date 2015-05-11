# -*- encoding: utf-8 -*-
from django.db import models
from decimal import Decimal

from core.models import TimeStampedModel, CancelledModel


class UnidadMedida(models.Model):
    unidad = models.CharField(max_length=15, unique=True)
    prefix = models.CharField(max_length=4)

    def __unicode__(self):
        return '%s (%s)' % (self.unidad, self.prefix)


class Producto(TimeStampedModel):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=120)
    unidad_medida = models.ForeignKey(UnidadMedida)
    porciones = models.IntegerField(max_length=5, default=0)
    precio_porcion = models.DecimalField(max_digits=8, decimal_places=2,
                                         default=Decimal(u'0.00'))
    is_inactive = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.unidad_medida)

    def get_stock(self):
        ''' Regresa cantidad disponible. '''
        return self.porciones

    def in_stock(self):
        ''' Regresa True si esta en stock. '''
        return self.get_stock() > 0

    def agregar(self, cantidad):
        self.porciones += cantidad

    def quitar(self, cantidad):
        porciones = self.porciones - cantidad
        return porciones


class Entrada(TimeStampedModel):
    ''' Entrada de cantidad en producto (porciones) '''
    producto = models.ForeignKey(Producto)
    porciones = models.IntegerField(max_length=5, default=0)
    is_cancelled = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.producto


class CancelEntrada(CancelledModel):
    '''
    Hereda del modelo abstracto CancelledModel.
    Agrega relacion con la entrada a cancelar.
    '''
    entrada = models.ForeignKey(Entrada)

    def __unicode__(self):
        return '%s' % self.reason
