from django.db import models

# Create your models here.

class Hystogramservices (models.Model):

	procedimientorealizado=models.ForeignKey(Cotizacion)
	nombre_paciente=models.ForeignKey(Paciente)
	nombre_medico=models.ForeignKey(Medico)

class Hystogramrepo(models.Model):

	procedimiento =models.ManytoManyField(Hystogramservices)
	startdate=models.DateField()
	finishdate=models.DateField()
	

