from django.db import models
from altas.models import Medico,Paciente
from precios.models import PrecioServicio
from precios.models import GrupoServicio
from decimal import Decimal






class Cotizacion (models.Model):
	fecha=models.DateTimeField(auto_now_add=True)
	paciente=models.ForeignKey(Paciente)
	medico =models.ForeignKey(Medico)
	def __unicode__(self):
		return'['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+'] ' + self.paciente.nombre + self.medico.nombre
	def total (self):
		cotizaciondetails=CotizacionDetail.objects.filter(cotizacion__id__exact=self.id)
		total=0
		for cotizaciondetail in cotizaciondetails:
			total+=cotizaciondetail.cantida*cotizaciondetail.servicio.precio
		return total



class CotizacionDetail(models.Model):
	cotizacion=models.ForeignKey(Cotizacion)
	servicio=models.ForeignKey(GrupoServicio)
	cantidad = models.DecimalField(max_digits = 5, decimal_places = 2)

	def total(self):
		total=self.cantidad*self.servicio.precio
		return total







