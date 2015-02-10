from django.db import models
from altas.models import Medico,Paciente
from precios.models import PrecioServicio
from precios.models import GrupoServicio





# Create your models here.
class cotizacion(models.Model):
	folio_cotizacion	=models.CharField(max_length=8)
	fechaEntrada		= models.DateField(blank=True, null=True)
	nombre_doctor		=models.ForeignKey(Medico)
 	nombrepaciente		=models.ForeignKey(Paciente)
 	nombreservicio		=models.ManyToManyField(PrecioServicio,null=True,blank=True)
 	precios       		=models.ForeignKey(GrupoServicio)
 	status        		= models.BooleanField(default=True)
 	granTotal    	   	=models.CharField(max_length=10)

 	

 	def __unicode__(self):
 		codigo="%s"%(self.folio_cotizacion)
 		return codigo



