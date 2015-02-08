from django.db import models 
from altas.models import Medico,Paciente

#from django.contrib import models

# Create your models here.


class Interrogatorio(models.Model):
	paciente	= models.ForeignKey(Paciente)
	medico	= models.ForeignKey(Medico)
	ultimaVisitaMedico = models.CharField(max_length=100, null=False)
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

		nombres ="%s %s "% (self.paciente,self.medico)
		return nombres


 


class ListadeDiagnosticos(models.Model):
	CIE10=models.CharField(max_length=15)
	CDi=models.CharField(max_length=15)
	nomDi=models.CharField(max_length=30)
	def __unicode__(self):
		codigoCie="%s  %s"%(self.CIE10)
		return CO

class Odontograma(models.Model):
 	nombre_doctor=models.ForeignKey(Medico)
 	nombrepaciente=models.ForeignKey(Paciente)
 	fechayHora = models.DateTimeField(blank=True, null=True)
 	nombrePiezaDental=models.CharField(max_length=40)
 	problemaDental=models.ForeignKey(ListadeDiagnosticos)
 	notas=models.TextField()
 	
 	def __unicode__(self):
 		problema="%s  %s"% (self.problemaDental)
 		return problema






