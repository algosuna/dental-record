from decimal import Decimal

from django.db import models

from altas.models import Medico, Paciente
from precios.models import PrecioServicio, GrupoServicio, GrupoPrecios
from ActividadesClinicas.models import Procedimiento,Tratamiento

class Cotizacion(models.Model):
	id=models.AutoField(primary_key=True,null=False)
	fecha = models.DateTimeField(auto_now_add = True)
	paciente = models.ForeignKey(Paciente,null=True)
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
	nombreDelServicio = models.ForeignKey(Tratamiento)
	nombreDelGrupo = models.ForeignKey(GrupoPrecios)
	precio = models.DecimalField(max_digits=19, decimal_places=3)

	def __unicode__(self):
		return "%s (%s)"%(self.nombreDelServicio ,self.precio)

class CotizacionDetail(models.Model):
	estado_CHOICES=(
		('aceptado','aceptado'),
		('pendiente','pendiente'),
		)
	estado      =models.CharField(max_length=10,choices=estado_CHOICES,default='aceptdado')
	cotizacion  = models.ForeignKey(Cotizacion)
	servicio    = models.ForeignKey(CatalogodeServicios)

	def __unicode__(self):
		return "(%s) %s"%(self.cotizacion,self.servicio)

	def total(self):
		total = self.precio
		return total


