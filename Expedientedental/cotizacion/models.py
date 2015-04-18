from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Sum

from core.models import TimeStampedModel
from clinica.models import Procedimiento, Odontograma
from precios.models import PrecioTratamiento


class Cotizacion(TimeStampedModel):
    odontograma = models.ForeignKey(Odontograma, null=True)

    def total(self):
        resultado = self.cotizacionitem_set.total()
        return resultado

    def total_aceptado(self):
        resultado = self.cotizacionitem_set.aceptados().total()
        return resultado

    def total_procesado(self):
        resultado = self.cotizacionitem_set.procesados().total()
        return resultado

    def __unicode__(self):
        cotizacion = "cotizacion %s" % (self.odontograma)
        return cotizacion


class CotizacionItemQuerySet(QuerySet):

    def total(self):
        resultado = self.aggregate(Sum('precio'))
        if resultado['precio__sum'] is None:
            return 0
        return resultado['precio__sum']


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

    def get_query_set(self):
        return CotizacionItemQuerySet(self.model, using=self._db)

    def total(self):
        return self.get_query_set().total()

    def procesados(self):
        return self.filter(status='procesado')

    def aceptados(self):
        return self.filter(status='aceptado')


class CotizacionItem(TimeStampedModel):
    STATUS_CHOICES = (
        ('aceptado', 'Aceptado'),
        ('pendiente', 'Pendiente'),
        ('procesado', 'Procesado')
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pendiente')
    cotizacion = models.ForeignKey(Cotizacion)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    procedimiento = models.ForeignKey(Procedimiento)

    objects = CotizacionItemManager()

    def __unicode__(self):
        return " %s" % (self.procedimiento)
