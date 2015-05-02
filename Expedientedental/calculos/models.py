from django.db import models
from servicios.models import Servicio
from paquete.models import PaqueteConsumidoItem

# Create your models here.


class Dolar(models.Model):
    costo = models.DecimalField(max_digits=8, decimal_places=2)


class Utilidad (models.Model):
    precio_servicio = models.ForeignKey(Servicio)
    costo_paquete = models.ForeignKey(PaqueteConsumidoItem)
    utilidad = models.DecimalField(max_digits=8, decimal_places=2)
    costo_dolar = models.ForeignKey(Dolar)

    def obtener(self):
        utilidad = self.precio_servicio/self.costo_paquete
        return '%s' % utilidad

    def conversionutilidad(self):
        util = self.utilidad * self.costo
        return '%s' % util 