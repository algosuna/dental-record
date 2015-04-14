# -*- encoding: utf-8 -*-
from django.db import models
import datetime as dt
from altas.models import Medico, Paciente
from pagos.models import PagoAplicado


class Paquete(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return'%s' % (self.nombre)


class PaqueteItem(models.Model):
    paquete = models.ForeignKey(Paquete)
    producto = models.ForeignKey('Inventario.Producto')
    cantidad_producto = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return '%s' % (self.paquete)


class PaqueteConsumido(models.Model):
    paquete = models.ForeignKey(Paquete)
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateTimeField()

    def __unicode__(self):
        return '%s %s' % (self.paquete, self.medico)


class PaqueteConsumidoItem(models.Model):
    paquete_consumido = models.ForeignKey(PaqueteConsumido)
    tratamiento_pago = models.ForeignKey(PagoAplicado)
    producto = models.ForeignKey('Inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return u'%s %s %s ' % (self.producto, self.cantidad, self.precio)
