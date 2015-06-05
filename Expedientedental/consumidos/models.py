# -*- encoding: utf-8 -*-
from django.db import models
from django.db.models import Sum
from altas.models import Medico, Paciente
from core.models import CancelledModel, TimeStampedModel


class Paquete(models.Model):
    '''
    Los Paquetes se usan para agrupar Productos necesarios para realizar
    un 'servicio' o 'procedimiento'. Facilita el proceso de la persona en
    inventario. Deben ser creados previamente y se necesita familarizacion
    con los 'servicios' o 'procedimientos'.
    '''
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200)
    productos = models.ManyToManyField('inventario.Producto',
                                       through='PaqueteItem')

    is_inactive = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.nombre


class PaqueteItem(models.Model):
    ''' Productos de un paquete. '''
    paquete = models.ForeignKey(Paquete)
    producto = models.ForeignKey('inventario.Producto')
    cantidad_producto = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return '%s' % self.paquete


class PaqueteConsumido(TimeStampedModel):
    ''' Indica un grupo de productos que saldran de inventario. '''
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
        return '%s %s %s' % (self.paquete, self.medico, self.status)

    def get_item_initials(self):
        ''' Asigna initials usando PaqueteItems con ForeignKey a Paquete. '''
        paquete = self.paquete
        paquete_items = paquete.paqueteitem_set.filter(
            producto__is_inactive=False)
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

    def precio_total(self):
        ''' Saca el total de todos los PaqueteConsumidoItems con ForeignKey
        a PaqueteConsumido. '''
        return self.paqueteconsumidoitem_set.get_precio_total()


class PaqueteConsumidoItemManager(models.Manager):
    def get_precio_total(self):
        ''' Suma el precio de PaqueteConsumidoItem. '''
        precio = self.aggregate(Sum('precio'))['precio__sum']
        if precio is None:
            precio = 0
        return precio


class PaqueteConsumidoItem(models.Model):
    '''
    Producto a salir de inventario. Contiene el precio de acorde al precio
    del producto y la cantidad que va de salida (se consume).
    '''
    paquete_consumido = models.ForeignKey(PaqueteConsumido)
    producto = models.ForeignKey('inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    objects = PaqueteConsumidoItemManager()

    def __unicode__(self):
        return u'%s %s %s' % (self.producto, self.cantidad, self.precio)

    def set_precio(self):
        ''' Calcula el precio correcto a asignar multiplicando el precio
        del producto por la cantidad de este. '''
        precio = self.producto.precio_porcion * self.cantidad
        return precio


class ProductoConsumido(models.Model):
    '''
    Saca Productos de inventario sin necesidad de asociarse a un servicio
    y sin generar peticion (PaqueteConsumido).
    '''
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    producto = models.ForeignKey('inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s %s' % (self.producto, self.cantidad, self.cantidad)


class CancelPaquete(CancelledModel):
    paquete = models.ForeignKey(Paquete)

    def __unicode__(self):
        return '%s' % self.reason


class CancelSalida(CancelledModel):
    '''
    Hereda del modelo abstracto CancelledModel que contiene 'motivo'
    y 'created_at'. Agrega relacion con la salida a cancelar.
    '''
    salida = models.ForeignKey(ProductoConsumido)

    def __unicode__(self):
        return '%s' % self.reason
