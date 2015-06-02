# -*- encoding: utf-8 -*-
from django.db import models
from altas.models import Medico, Paciente
from core.models import CancelledModel, TimeStampedModel


class Paquete(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return'%s' % (self.nombre)


class PaqueteItem(models.Model):
    paquete = models.ForeignKey(Paquete)
    producto = models.ForeignKey('inventario.Producto')
    cantidad_producto = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return '%s' % (self.paquete)


class PaqueteConsumido(TimeStampedModel):
    STATUS_CHOICES = (
        ('en_espera', 'En Espera'),
        ('por_entregar', 'Por Entregar'),
        ('cancelado', 'Cancelado'),
        ('surtido', 'Surtido'),
    )
    paquete = models.ForeignKey(Paquete, null=True)
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    servicio = models.ForeignKey('servicios.Servicio', null=True)
    nota = models.TextField(blank=True)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='en_espera')

    def __unicode__(self):
        return '%s %s' % (self.paquete, self.medico, self.status)

    def get_item_initials(self):
        paquete = self.paquete
        paquete_items = paquete.paqueteitem_set.all()
        initial_list = []
        for pitem in paquete_items:
            initial = {
                'paquete_consumido': self,
                'producto': pitem.producto,
                'cantidad': pitem.cantidad_producto,
                'precio': pitem.producto.precio_porcion
            }
            initial_list.append(initial)
        return initial_list


class PaqueteConsumidoItem(models.Model):
    paquete_consumido = models.ForeignKey(PaqueteConsumido)
    producto = models.ForeignKey('inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return u'%s %s %s ' % (self.producto, self.cantidad, self.precio)

    def set_precio(self):
        precio = self.producto.precio_porcion * self.cantidad
        return precio


class ProductoConsumido(models.Model):
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    producto = models.ForeignKey('inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s %s' % (
            self.producto, self.cantidad, self.cantidad)


class CancelSalida(CancelledModel):
    '''
    Hereda del modelo abstracto CancelledModel.
    Agrega relacion con la salida a cancelar.
    '''
    salida = models.ForeignKey(ProductoConsumido)

    def __unicode__(self):
        return '%s' % self.reason
