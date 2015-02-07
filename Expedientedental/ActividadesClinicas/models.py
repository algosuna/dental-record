from django.db import models


# Create your models here.


class interrogatorio(models.Model):
	nombrepaciente	= models.ForeignKey('nombre.paciente')
	nombredoctor	= models.ForeignKey('nombre.medico')
	credencial_paciente = models.ForeignKey('credencial_paciente.paciente')
	ultimaVisitaMedico = models.CharField(max_length=100, null=False)
	medicamentoultimosdosanios = models.CharField(max_length=100, null=False)
	alergicoamedicamentos = models.CharField(max_length=100, null=False)
	alergicoaanestesicos = models.CharField(max_length=100, null=False)
	padeceenfermedades = models.CharField(max_length=100, null=False)
	enfermedad_trasmision_sexual = models.CharField(max_length=100, null=False)
	otraEnfermedad = models.CharField(max_length=100, null=False)
	estaEmbarazada = models.CharField(max_length=100, null=False)
	observaciones = models.TextField()
	resumenClinico = models.TextField()

 


class listadeDiagnosticos(models.Model):
	CIE10=models.CharField(foreign_key=True,max_length=15)
	CDi=models.CharField(primary_key=True,max_length=15)
	nomDi=models.CharField(max_length=30)
	def __unicode__(self):
		codigoCie="% %"%(self.CIE10)
		return CO

class Odontograma(models.Model):
 	nombre_doctor=models.ForeignKey('nombre.medico')



class listadiagnospor paciente(models.Model):
	id_paciente=models.CharField(foreign_key=True,max_length=5)
	nom_pacient=models.CharField(foreign_key=True,max_length=50)
	id_med=models.CharField(foreign_key=True, max_length=5)
	codigoDiagnostico=models.CharField(foreign_key=True,max_length=15)
	CIE10=models.CharField(foreign_key=True,max_length=15)
	nomDiagnostico=models.CharField(foreignkey=True,max_length=30)



