from django.db import models
from django.db.models import Sum
from django.db.models.query import QuerySet

from core.models import TimeStampedModel
from clinica.models import Odontograma, Procedimiento
from pagos.models import PagoAplicado


class Paquete(TimeStampedModel):
    odontograma = models.ForeignKey(Odontograma)

    def total(self):
        '''
        suma aceptado, parcial, pagado
        '''
        r = self.servicio_set.total()
        return r

    def total_adeudado(self):
        r = self.servicio_set.total_adeudado()
        return r

    def total_pagado(self):
        r = self.servicio_set.total_pagado()
        return r

    def total_adeudo(self):
        s = self.servicio_set.filter(status__in=['parcial', 'aceptado'])
        r = s.total_adeudado()
        return r

    def total_pago(self):
        s = self.servicio_set.filter(status__in=['parcial', 'pagado'])
        r = s.total_pagado()
        return r

    def __unicode__(self):
        paquete = 'Paquete de Servicios %s' % (self.odontograma)
        return paquete


class ServicioQuerySet(QuerySet):

    def total(self):
        r = self.aggregate(Sum('precio'))

        if r['precio__sum'] is None:
            return 0

        return r['precio__sum']

    def total_pagado(self):
        pa_qs = PagoAplicado.objects.filter(servicio__in=self)

        if not pa_qs.exists():
            return 0

        total_pagado = pa_qs.aggregate(Sum('importe'))

        return total_pagado['importe__sum']

    def total_adeudado(self):
        return max(0, self.total() - self.total_pagado())


class ServicioManager(models.Manager):
    def create_servicios(self, paquete, cotizacion):
        cotizacionitems = cotizacion.cotizacionitem_set.aceptados()

        servicios = []

        for item in cotizacionitems:

            servicio = self.create(
                status='aceptado',
                paquete=paquete,
                precio=item.precio,
                procedimiento=item.procedimiento
            )
            servicios.append(servicio)

            item.status = 'procesado'
            item.save()

        return servicios

    def get_query_set(self):
        return ServicioQuerySet(self.model, using=self._db)

    def total(self):
        return self.get_query_set().total()

    def total_pagado(self):
        return self.get_query_set().total_pagado()

    def total_adeudado(self):
        return self.get_query_set().total_adeudado()


class Servicio(TimeStampedModel):
    STATUS_CHOICES = (
        ('aceptado', 'Aceptado'),
        ('parcial', 'Pago Parcial'),
        ('pagado', 'Pagado'),
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='aceptado')
    paquete = models.ForeignKey(Paquete)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    procedimiento = models.ForeignKey(Procedimiento)

    objects = ServicioManager()

    def __unicode__(self):
        return "Servicio %s" % (self.procedimiento)
