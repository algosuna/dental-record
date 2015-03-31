from django.db import models

from cotizacion.models import CotizacionItem


class DateTime(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.fecha.strftime("%b %d, %Y, %I:%M %p"))


class Pago(models.Model):
	fecha=models.DateTimeField(DateTime)
	monto=models.DecimalField(max_digits = 6, decimal_places = 2)
	detalles=models.CharField(max_length=50)

	def __unicode__(self):
		pagodetalle ="%s %s %s "% (self.fecha,self.monto,self.detalles)
		return pagodetalle



class SeervAut(models.Model):
	servicio=models.ForeignKey(CotizacionItem)
	total=models.DecimalField(max_digits=19, decimal_places=10)

	def __unicode__(self):
		servicio="%s"%(self.servicio)
		return servicio


class procesoPago(models.Model):
	fecha=models.DateTimeField(auto_now_add=True)
	servicio=models.ForeignKey(SeervAut)
	movpago=models.ForeignKey(Pago)
	saldoAnterior=models.DecimalField( max_digits=19, decimal_places=10)
	saldoActual=models.DecimalField( max_digits=19, decimal_places=10)


	def __unicode__(self):
		servicio ="%s"%(self.servicio)
		return servicio
