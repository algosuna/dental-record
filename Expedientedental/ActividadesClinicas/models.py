from django.db import models 
from altas.models import Medico,Paciente
from datetime import date

#from django.contrib import models

# Create your models here.

class HistoriaClinica(models.Model):
	auxBucal_CHOICES=(

		('Si', 'Si'),
        ('No', 'No'),
        )
	chatarra_CHOICES=(

    	('Si', 'Si'),
        ('No', 'No'),
        

    	)
	cartilla_CHOICES=(

		('Si', 'Si'),
        ('No', 'No'),
        
		)
	esquema_Choices=(
		('Si', 'Si'),
        ('No', 'No'),

        )

	antecedentes_Choices=(
		('Tabaco', 'Tabaco'),
        ('Alcohol', 'Alcohol'),
        
        )
	alergias_CHOICES=(

		('Antibioticos', 'Antibioticos'),
        ('Analgesicos', 'Analgesicos'),
        ('Anestesicos','Alimentos')
        )
	hospital_CHOICES=(
		('Si', 'Si'),
        ('No', 'No'),
        )
	#exploracion
	cabeza_CHOICES=(
		('Exotosis', 'Exotosis'),
        ('Endostosis', 'Endostosis'),
        
        )
	craneo_CHOICES=(
		('Dolicocefalico', 'Dolicocefalico'),
        ('Mesocefalico','Mesocefalico'),
        
        )
	cara_CHOICES=(
		('Asimetrias:Transversales','Asimetrias:Transversales'),
        ('longitudinales','longitudinales'),
        )
	perfil_CHOICES=(
		('Concavo', 'Concavo'),
        ('Convexo', 'Convexo'),
        ('Recto','Recto'),
        )
	piel_CHOICES=(
		('Normal', 'Normal'),
        ('Palida', 'Palida'),
        ('Cianotica','Cianotica'),
        ('Enrojecida','Enrojecida'),
        )
	musculos_CHOICES=(
		('hipnoticos', 'hipnoticos'),
        ('hipernoticos', 'hipernoticos'),
        ('espasticos', 'espasticos'),
        )
	cuello_CHOICES=(
		('Si', 'Si'),
        ('No', 'No'),
        )
	cuello_CHOICES=(
		('Si', 'Si'),
        ('No', 'No'),
        )
	cuello_CHOICES=(
		('Si', 'Si'),
        ('No', 'No'),
        )
	grupoSanguineo_CHOICES=(
		('AB+','AB+'),
		('AB-','AB-'),
		('A+','A+'),
		('A-','A-'),
		('B+','B+'),
		('B-','B-'),
		('O+','O+'),
		('O-','O-'),

		)
	
	#articulacion temporomandibular
	ruidos_CHOICES=(
		('Si','No'),
		('No','No'),
		('Lateralidad','Lateralidad'),
		('Apertura','Apertura'),
		)
	chasquidos_CHOICES=(
		('Si','Si'),
		('No','No'),
		)
	crepitacion_CHOICES=(
		('Si','Si'),
		('No','No'),
		)
	dificultadParaAbrirLaBoca_CHOICES=(
		('Si','Si'),
		('No','No'),
		)
	dolorabertura_CHOICES=(
		('Si','Si'),
		('No','No'),
		)
	fatigadolormuscular_CHOICES=(
		('Si','Si'),
		('No','No'),
		)
	disminuciondelaavertura_CHOICES=(
		('Si','Si'),
		('No','No'),
		)
	desviacionaverturadecierre_CHOICES=(
		('Si','Si'),
		('No','No'),
		)

	paciente	= models.ForeignKey(Paciente)
	medico	= models.ForeignKey(Medico)
	ultimaVisitaMedica = models.DateTimeField(auto_now_add=True)
	herenciaPatologicaopciones=models.CharField(max_length=50)
	herenciaMadre=models.CharField(max_length=50)
	herenciaPadre=models.CharField(max_length=50)
	herenciaHermanos=models.CharField(max_length=50)
	herenciaHijos=models.CharField(max_length=50)
	herenciaEsposos=models.CharField(max_length=50)
	herenciaTios=models.CharField(max_length=50)
	herenciaAbuelos=models.CharField(max_length=50)
	eInflamatoriasnotopciones=models.TextField()
	ets=models.TextField()
	eDegenerativas=models.TextField()
	eNeoplasticas=models.TextField()
	eCongenitas=models.TextField()
	otras=models.TextField()
	habitosHigienicosVest=models.TextField()
	habitosHigienicosCorp=models.TextField()
	frecuenciaLavadoDental=models.TextField()
	uxiliaresBucales=models.CharField(max_length=2,choices=auxBucal_CHOICES)
	consumodeGolosinas=models.CharField(max_length=2,choices=chatarra_CHOICES)
	gruposanguineo=models.CharField(max_length=20,choices=grupoSanguineo_CHOICES)
	factorRh=models.CharField(max_length=5)
	cartilladeVacunacion=models.CharField(max_length=2,choices=cartilla_CHOICES)
	esquemaCompleto=models.CharField(max_length=2,choices=esquema_Choices)
	esquemaFalta=models.CharField(max_length=200)
	adicciones=models.CharField(max_length=15,choices=antecedentes_Choices)
	alergias=models.CharField(max_length=400,choices=alergias_CHOICES)
	fechaHospitalizaion=models.DateTimeField(choices=hospital_CHOICES)
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
	cabeza=models.CharField(max_length=400,choices=cabeza_CHOICES)
	craneo=models.CharField(max_length=50,choices=craneo_CHOICES)
	caraAsimetria=models.CharField(max_length=20,choices=cara_CHOICES)
	perfil= models.CharField(max_length=15,choices=perfil_CHOICES)
	piel=models.CharField(max_length=50,choices=piel_CHOICES)
	musculos=models.CharField(max_length=500)
	cuello=models.CharField(max_length=15,choices=cuello_CHOICES)
	otros=models.CharField(max_length=50)
	ruidos=models.CharField(max_length=35)
	chasquidos=models.CharField(max_length=15,choices=chasquidos_CHOICES)
	crepitacion=models.CharField(max_length=15,choices=crepitacion_CHOICES)
	difparaAbrirlaboca=models.CharField(max_length=15,choices=dificultadParaAbrirLaBoca_CHOICES)
	dolorabertura=models.CharField(max_length=15,choices=dolorabertura_CHOICES)
	fatigadolormuscular=models.CharField(max_length=15,choices=fatigadolormuscular_CHOICES)
	disminuciondelaavertura=models.CharField(max_length=10,choices=disminuciondelaavertura_CHOICES)
	desviacionaverturadecierre=models.CharField(max_length=10,choices=desviacionaverturadecierre_CHOICES)
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



