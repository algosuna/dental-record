from django.db import models
from django.db.models import Sum

from core.models import TimeStampedModel
from altas.models import Paciente


class Pago(TimeStampedModel):
    '''
    Monto que da el cliente.
    Este modelo permite que el pago se asigne a mas de una cotizacion.
    '''
    fecha = models.DateField()  # fecha en que se da el pago
    servicios = models.ManyToManyField(
        'servicios.Servicio', through='PagoAplicado')
    # lo que el cliente da / monto a aplicar
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    # lo que se aplica a items / lo que se ha consumido del pago(monto)
    monto_aplicado = models.DecimalField(
        max_digits=9, decimal_places=3, default=0)
    paciente = models.ForeignKey(Paciente)

    def montodisponible(self):
        '''
        Cuanto queda de credito (saldo a favor).
        '''
        resta = self.monto - self.monto_aplicado
        return resta

    def aplicamonto(self, monto_a_aplicar):
        '''
        Metodo setter para mantener un monto_aplicado valido.
        monto_aplicado debe ser menor o igual a monto.
        '''
        if monto_a_aplicar == self.montodisponible():
            aplica = self.monto_aplicado + monto_a_aplicar
            self.monto_aplicado = aplica
        else:
            raise ValueError('No se pudo aplicar monto')

    def __unicode__(self):
            pago = "%s %s %s" % (self.monto, self.monto_aplicado, self.fecha)
            return pago


class PagoAplicadoManager(models.Manager):

    def total_pagado(self):
        pa_qs = self.all()
        if not pa_qs.exists():
            return 0
        total_pagado = pa_qs.aggregate(Sum('importe'))
        return total_pagado['importe__sum']


class PagoAplicado(models.Model):
    '''
    Tabla puente entre Pago y CotizacionItem. Asigna cantidad por item.
    '''
    pago = models.ForeignKey(Pago)
    servicio = models.ForeignKey('servicios.Servicio')
    fecha = models.DateTimeField(auto_now_add=True)
    # aqui se aplica parte del pago para un item
    importe = models.DecimalField(max_digits=6, decimal_places=2)

    objects = PagoAplicadoManager()

    def __unicode__(self):
            pagodetalle = "%s %s" % (self.pago, self.servicio)
            return pagodetalle
