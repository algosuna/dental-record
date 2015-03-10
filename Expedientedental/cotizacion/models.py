from django.db import models
from altas.models import Medico,Paciente
from precios.models import PrecioServicio
from precios.models import GrupoServicio
from precios.models import GrupoPrecios
from ActividadesClinicas.models import Procedimiento
from decimal import Decimal







class Cotizacion(models.Model):
	folio =models.CharField(max_length=9,unique = True)
	fecha = models.DateTimeField(auto_now_add = True)
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
	total=models.DecimalField(max_digits=19, decimal_places=10)


	def __unicode__(self):
		return '['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+']  '+self.paciente.nombre+' '+self.paciente.apellidoPaterno
	
	def total(self):
		cotizaciondetails = CotizacionDetail.objects.filter(cotizacion__id__exact = self.id)
		total = 0
		for cotizaciondetail in cotizaciondetails:
			total += cotizaciondetail.servicio.precio
		return total


class CatalogodeServicios(models.Model):
	nombreDelServicio = models.ForeignKey(PrecioServicio)
	nombreDelGrupo = models.ForeignKey(GrupoPrecios)
	precio = models.OneToOneField(GrupoServicio,null=True)
	
	def __unicode__(self):
		return "%s (%s)"%(self.nombreDelServicio ,self.precio)
		 


class CotizacionDetail(models.Model):
	estado_CHOICES=(

		('aceptado','aceptado'),
		('pendiente','pendiente'),


		)
	estado      =models.CharField(max_length=10,choices=estado_CHOICES,default='aceptado')
	cotizacion  = models.ForeignKey(Cotizacion)
	servicio    = models.ForeignKey(CatalogodeServicios)
	diagnostico = models.ForeignKey(Procedimiento)

	def __unicode__(self):
		return "(%s) %s %s"%(self.cotizacion,self.servicio,self.diagnostico)

	def total(self):
		total = self.precio
		return total

	
