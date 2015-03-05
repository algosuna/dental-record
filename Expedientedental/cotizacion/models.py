from django.db import models
from altas.models import Medico,Paciente
from precios.models import PrecioServicio
from precios.models import GrupoServicio
from precios.models import GrupoPrecios
from decimal import Decimal



class Cotizacion(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)


	def __unicode__(self):
		return '['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+']  '+self.paciente.nombre+' '+self.paciente.apellidoPaterno
	
	def total(self):
		cotizaciondetails = CotizacionDetail.objects.filter(cotizacion__id__exact = self.id)
		total = 0
		for cotizaciondetail in cotizaciondetails:
			total += cotizaciondetail.precio
		return total

class CotizacionDetail(models.Model):
	cotizacion = models.ForeignKey(Cotizacion)
	nombreDelServicio = models.ForeignKey(PrecioServicio)
	nombreDelGrupo = models.ForeignKey(GrupoPrecios)
	precio = models.OneToOneField(GrupoServicio,null=True) 

	def total(self):
		total = self.precio
		return total

	def __unicode__(self):
		datos = "%s %s"%(self.nombreDelServicio,self.nombreDelGrupo)
		return datos

	def __unicode__(self):
		precio = "%s"%(self.precio)
		return precio
