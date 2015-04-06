from django.db import models

from core.models import TimeStampedModel
from clinica.models import Procedimiento, Odontograma
from precios.models import PrecioTratamiento
from django.db.models import Sum


class Cotizacion(TimeStampedModel):
    odontograma = models.ForeignKey(Odontograma, null=True)

    def total(self):
        resultado = self.cotizacionitem_set.total_aceptado()
        return resultado

    def __unicode__(self):
        cotizacion = "cotizacion %s" % (self.odontograma)
        return cotizacion


class CotizacionItemManager(models.Manager):
    def create_items(self, cotizacion):
        odontograma = cotizacion.odontograma

        procedimiento_qs = odontograma.procedimiento_set.all()
        grupo = odontograma.paciente.grupo

        items = []

        for procedimiento in procedimiento_qs:

            precio = PrecioTratamiento.objects.get(
                grupo=grupo,
                tratamiento=procedimiento.tratamiento
            ).precio
            item = self.create(
                status='pendiente',
                cotizacion=cotizacion,
                precio=precio,
                procedimiento=procedimiento
            )
            items.append(item)

        return items

    def total_aceptado(self):
        resultado = self.filter(status='aceptado').aggregate(Sum('precio'))
        return resultado['precio__sum']


class CotizacionItem(TimeStampedModel):
    STATUS_CHOICES = (
        ('aceptado', 'Aceptado'),
        ('pendiente', 'Pendiente'),
        ('parcial', 'Pago Parcial'),
        ('pagado', 'Pagado'),
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='aceptado')
    cotizacion = models.ForeignKey(Cotizacion)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    procedimiento = models.ForeignKey(Procedimiento)

    objects = CotizacionItemManager()

    def __unicode__(self):
        return " %s" % ( self.procedimiento)
