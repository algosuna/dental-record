from django.db import models
from django.db.models import Sum

from core.models import TimeStampedModel
from clinica.models import Odontograma, Procedimiento
from pagos.models import PagoAplicado


class Paquete(TimeStampedModel):
    odontograma = models.ForeignKey(Odontograma)

    def total(self):
        '''
        suma aceptado, parcial, pagado
        '''
        resultado = self.servicio_set.total()
        return resultado

    def total_adeudado(self):
        resultado = self.servicio_set.total_adeudado()
        return resultado

    def total_pagado(self):
        resultado = self.servicio_set.total_pagado()
        return resultado

    def total_adeudo(self):
        servicios = self.servicio_set.filter(status__in=['parcial', 'aceptado'])
        resultado = servicios.total_adeudado()
        return resultado

    def total_pago(self):
        servicios = self.servicio_set.filter(status__in=['parcial', 'pagado'])
        resultado = servicios.total_pagado()
        return resultado

    def __unicode__(self):
        paquete = 'Paquete de Servicios %s' % (self.odontograma)
        return paquete


class ServicioManager(models.Manager):
    def create_servicios(self, paquete, cotizacion):
        cotizacionitems = cotizacion.cotizacionitem_set.all()

        servicios = []

        for item in cotizacionitems:

            servicio = self.create(
                status='aceptado',
                paquete=paquete,
                precio=item.precio,
                procedimiento=item.procedimiento
            )
            servicios.append(servicio)

        return servicios

    def total(self):
        resultado = self.all().aggregate(Sum('precio'))
        if resultado['precio__sum'] is None:
            return 0
        return resultado['precio__sum']

    def total_pagado(self):
        pa_qs = PagoAplicado.objects.filter(cotizacion_item__in=self.all())
        if not pa_qs.exists():
            return 0
        total_pagado = pa_qs.aggregate(Sum('importe'))
        return total_pagado['importe__sum']

    def total_adeudado(self):
        return max(0, self.total() - self.total_pagado())


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
