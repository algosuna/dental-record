from django.db import models 
from altas.models import Medico,Paciente
from datetime import date

#from django.contrib import models

# Create your models here.


class Interrogatorio(models.Model):
	paciente	= models.ForeignKey(Paciente)
	medico	= models.ForeignKey(Medico)
	ultimaVisitaMedico = models.DateField(blank=True, null=True)
	medicamentoUltimosDosanios = models.CharField(max_length=100, null=False)
	alergicoamedicamentos = models.CharField(max_length=100, null=False)
	alergicoaanestesicos = models.CharField(max_length=100, null=False)
	padeceenfermedades = models.CharField(max_length=100, null=False)
	enfermedad_trasmision_sexual = models.CharField(max_length=100, null=False)
	otraEnfermedad = models.CharField(max_length=100, null=False)
	estaEmbarazada = models.CharField(max_length=100, null=False)
	observaciones = models.TextField()
	resumenClinico = models.TextField()

	def __unicode__(self):

		nombres ="%s %s %s %s"% (self.medico,self.paciente,self.observaciones,self.resumenClinico)
		return nombres


class ListadeDiagnosticos(models.Model):
	codigoDiagnostico=models.CharField(max_length=15)
	nombreDiagnostico=models.CharField(max_length=30)
	def __unicode__(self):

<<<<<<< HEAD
		codigoCie="%s  %s"%(self.codigoDiagnostico,self.nombreDiagnostico)
=======
		codigoCie="%s "%(self.CIE10)
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
		return codigoCie

class Odontograma(models.Model):
 	nombre_doctor=models.ForeignKey(Medico)
 	nombre_paciente=models.ForeignKey(Paciente)
 	fechayHora = models.DateTimeField(blank=True, null=True)
 	nombrePiezaDental=models.CharField(max_length=40)
 	problemaDental=models.ForeignKey(ListadeDiagnosticos)
 	notas=models.TextField()
 	
 	def __unicode__(self):
<<<<<<< HEAD
 		problema="%s"% (self.problemaDental)
=======
 		
 		problema="%s  "% (self.problemaDental)
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
 		return problema



