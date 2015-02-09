from django.db import models
from datetime import date

# Create your models here.

# Modelo de Notas Agregadas

class Notas(models.Model):
	descripcion	= models.TextField()
	fechayHora = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		Nota = "%s %s"%(self.descripcion,self.fechayHora)
		return Nota


# Modelo de Bitacora de Procedimientos

class Bitacora(models.Model):
	nombredelProcedimiento = models.CharField(max_length=70)
	fechayhora = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):

		DatosBitacora = "%s %s"%(self.nombredelProcedimiento,self.fechayhora)
		return DatosBitacora

