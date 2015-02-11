from django.db import models
from altas.models import Medico,Paciente
from precios.models import PrecioServicio
from precios.models import GrupoServicio
from decimal import Decimal
from django.forms.models import BaseInlineFormSet, inlineformset_factory







# Create your models here.
#modelo para generar la cotizacion
class Cotizacion(models.Model):
	nodeCotizacion =models.CharField(max_length=25)   
	fecha = models.DateTimeField(auto_now_add=True,null=True)
	datosmedico=models.ForeignKey(Medico)
	datospaciente = models.ForeignKey(Paciente)
	productos = models.ManyToManyField(GrupoServicio)
       
       #dando preformato a la salida de texto
	def __unicode__(self):
		return '%s '% (self.nodeCotizacion)

class CotizacionServicios(models.Model):
	#relaciono con modelo de cotizacion
	cotizacion=models.ForeignKey(Cotizacion)
	servicio=models.ForeignKey(GrupoServicio)
	numero_servicios=models.DecimalField(max_digits=10,decimal_places=0)
	precio = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))



