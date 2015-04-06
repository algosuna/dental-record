from django.db import models
from core.models import TimeStampedModel
from cotizacion.models import CotizacionItem


class Pago(TimeStampedModel):



    
        fecha = models.DateTimeField()
        cotizacion_items = models.ManyToManyField(
            CotizacionItem, through='PagoAplicado')
        monto = models.DecimalField(max_digits=9, decimal_places=3)  # lo que el cliente debe
        monto_aplicado = models.DecimalField(
            max_digits=9, decimal_places=3, default=0)  # dependiendo de lo que abone este se aplica al tratamiento

        def montodisponible(self):
            resta = self.monto-self.monto_aplicado
            return resta

        def aplicamonto(self, monto_a_aplicar):

            if monto_a_aplicar <= self.montodisponible():
                aplica = self.monto_aplicado + monto_a_aplicar
                self.monto_aplicado = aplica

        def status(self):
            if self.monto_aplicado == 0:
                return 'No Aplicado'

            if self.monto == self.monto_aplicado:
                return 'Aplicado'

            return 'Parcialmente Aplicado'

        def __unicode__(self):
            pago = "%s %s %s " % (self.monto, self.monto_aplicado, self.fecha)
            return pago


class PagoAplicado(models.Model):
        pago = models.ForeignKey(Pago)
        cotizacion_item = models.ForeignKey(CotizacionItem)
        fecha = models.DateTimeField(auto_now_add=True)
        importe = models.DecimalField(max_digits=6, decimal_places=3) # aqui se despliega si esta cubierto o no 

        def __unicode__(self):
            pagodetalle = "%s %s" % (self.pago, self.cotizacion_item)
            return pagodetalle
