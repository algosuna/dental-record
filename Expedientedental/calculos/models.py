from django.db import models
from servicios.models import Servicio
from consumidos.models import PaqueteConsumidoItem

# Create your models here.


class Dolar(models.Model):
    costo = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        cambio = "%s" % (self.costo)
        return cambio


