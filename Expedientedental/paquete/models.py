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

    def get_item_initials(self):
        paquete = self.paquete
        paquete_items = paquete.paqueteitem_set.all()
        initial_list = []
        for pitem in paquete_items:
            initial = {
                'paquete_consumido': self,
                'producto': pitem.producto,
                'cantidad': pitem.cantidad_producto,
                'precio': pitem.producto.precioUnidad
            }
            initial_list.append(initial)
        return initial_list


class PaqueteConsumidoItem(models.Model):
    paquete_consumido = models.ForeignKey(PaqueteConsumido)
    producto = models.ForeignKey('Inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    #def stock(slef):
        # disponible = 
        # return disponible

    def disminuir(self, stock):
                if self.cantidad >= self.stock:
                        self.cantidad -= stock
                        return True
                return False

    def __unicode__(self):
        return u'%s %s %s ' % (self.producto, self.cantidad, self.precio)

    # TODO: metodo save debe restar unidades de inventario (consumir)
    # TODO: metodo delete debe sumar unidades de inventario (devoluciones)