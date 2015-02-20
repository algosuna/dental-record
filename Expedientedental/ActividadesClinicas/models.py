from django.db import models 
from altas.models import Medico,Paciente
from datetime import date

#from django.contrib import models

# Create your models here.

class HistoriaClinica(models.Model):
	paciente	= models.ForeignKey(Paciente)
	medico	= models.ForeignKey(Medico)
	ultimaVisitaMedica = models.DateTimeField(auto_now_add=True)
	herenciaPatologicaopciones=models.CharField(max_length=50)
	eInflamatoriasnotopciones=models.TextField()
	ets=models.TextField()
	eDegenerativas=models.TextField()
	eNeoplasticas=models.TextField()
	eCongenitas=models.TextField()
	otras=models.TextField()
	habitosHigienicosVest=models.TextField()
	habitosHigienicosCorp=models.TextField()
	frecuenciaLavadoDental=models.TextField()
	uxiliaresBucales=models.BooleanField()
	consumodeGolosinas=models.BooleanField()
	gruposanguineo=models.CharField(max_length=20)
	factorRh=models.CharField(max_length=5)
	cartilladeVacunacion=models.BooleanField()
	esquemaCompleto=models.BooleanField()
	esquemaFalta=models.CharField(max_length=200)
	adicciones=models.CharField(max_length=15)
	alergias=models.CharField(max_length=400)
	fechaHospitalizaion=models.DateTimeField()
	motivo=models.CharField(max_length=400)
	padecimientoActual=models.CharField(max_length=200)
	aparatoDigestivo=models.TextField()
	aparatoRespiratorio=models.TextField()
	aparatoCardioBascular=models.TextField()
	apararoGenitourinario=models.TextField()
	sistemaEndocrina=models.TextField()
	sistemaHemopoyetico=models.TextField()
	sistemamusculoEsqueletico=models.TextField()
	aparatoTegumentario=models.TextField()
	habitusExterior=models.TextField()
	peso=models.CharField(max_length=5)
	talla=models.CharField(max_length=10)
	complexion=models.CharField(max_length=15)
	frecuenciaCardiaca= models.CharField(max_length=15)
	tensionarterial=models.CharField(max_length=20)
	frecuenciaRespiratoria=models.CharField(max_length=50)
	temperatura=models.CharField(max_length=60)
	cabeza=models.CharField(max_length=400)
	craneo=models.CharField(max_length=50)
	caraAsimetria=models.CharField(max_length=20)
	perfil= models.CharField(max_length=15)
	piel=models.CharField(max_length=50)
	musculos=models.CharField(max_length=500)
	cuello=models.BooleanField()
	otros=models.CharField(max_length=50)
	ruidos=models.CharField(max_length=35)
	chasquidos=models.BooleanField()
	crepitacion=models.BooleanField()
	difparaAbrirlaboca=models.BooleanField()
	dolorabertura=models.BooleanField()
	fatigadolormuscular=models.BooleanField()
	disminuciondelaavertura=models.BooleanField()
	desviacionaverturadecierre=models.BooleanField()
	ganglios=models.TextField()
	glandulassalivales=models.TextField()
	labioExterno=models.TextField()
	bordebermellon=models.TextField()
	labiointerno=models.TextField()
	Comisuras=models.TextField()
	carrillos=models.TextField()
	fondodesaco=models.TextField()
	frenillos=models.TextField()
	lenguaTerciomedio=models.TextField()
	paladarDuro=models.TextField()
	paladarBlando=models.TextField()
	istmoBucofaringe=models.TextField()
	lenguaDorso=models.TextField()
	lenguaBordes=models.TextField()
	lenguaVentral=models.TextField()
	pisodelaBoca=models.TextField()
	dientes=models.TextField()
	mucosadelBordealveolar=models.TextField()
	encia=models.TextField()
	sistemaEndocrina=models.TextField()
	gingivitis=models.TextField()
	periodontitis=models.TextField()
	receciongingival=models.TextField()
	bolsasperiodontales=models.TextField()
	movilidadDentario=models.TextField()
	indicedeplaca=models.TextField()
	interpretacionradiografica=models.TextField()
	estudiosdeLaboratorio=models.TextField()
	interpretacionEstudiosLaboratorio=models.TextField()
	

	def __unicode__(self):

		nombres ="%s %s %s %s"% (self.medico,self.paciente,self.observaciones,self.resumenClinico)
		return nombres


class ListadeDiagnosticos(models.Model):
	codigoDiagnostico=models.CharField(max_length=15)
	nombreDiagnostico=models.CharField(max_length=30)
	
	def __unicode__(self):
		codigoCie="%s  %s"%(self.codigoDiagnostico,self.nombreDiagnostico)
		return codigoCie

class Odontograma(models.Model):
 	doctor=models.ForeignKey(Medico)
 	paciente=models.ForeignKey(Paciente)
 	fechayHora = models.DateTimeField(auto_now_add=True)
 	nombrePiezaDental=models.CharField(max_length=40)
 	problemaDental=models.ForeignKey(ListadeDiagnosticos)
 	notas=models.TextField()
 	
 	def __unicode__(self):
 		
 		problema="%s %s %s"% (self.doctor,self.paciente,self.fechayHora)
 		return problema



