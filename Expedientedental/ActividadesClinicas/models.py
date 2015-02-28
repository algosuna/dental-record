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
	herenciaMadre=models.CharField(max_length=50)
	herenciaPadre=models.CharField(max_length=50)
	herenciaHermanos=models.CharField(max_length=50)
	herenciaHijos=models.CharField(max_length=50)
	herenciaEsposos=models.CharField(max_length=50)
	herenciaTios=models.CharField(max_length=50)
	herenciaAbuelos=models.CharField(max_length=50)
	eInflamatoriasnotopciones=models.CharField(max_length=50)
	ets=models.CharField(max_length=50)
	eDegenerativas=models.CharField(max_length=50)
	eNeoplasticas=models.CharField(max_length=50)
	eCongenitas=models.CharField(max_length=50)
	otras=models.CharField(max_length=50)
	habitosHigienicosVest=models.CharField(max_length=50)
	habitosHigienicosCorp=models.CharField(max_length=50)
	frecuenciaLavadoDental=models.CharField(max_length=50)
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
	aparatoDigestivo=models.CharField(max_length=50)
	aparatoRespiratorio=models.CharField(max_length=50)
	aparatoCardioBascular=models.CharField(max_length=50)
	apararoGenitourinario=models.CharField(max_length=50)
	sistemaEndocrina=models.CharField(max_length=50)
	sistemaHemopoyetico=models.CharField(max_length=50)
	sistemamusculoEsqueletico=models.CharField(max_length=50)
	aparatoTegumentario=models.CharField(max_length=50)
	habitusExterior=models.CharField(max_length=50)
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
	ganglios=models.CharField(max_length=50)
	glandulassalivales=models.CharField(max_length=50)
	labioExterno=models.CharField(max_length=50)
	bordebermellon=models.CharField(max_length=50)
	labiointerno=models.CharField(max_length=50)
	Comisuras=models.CharField(max_length=50)
	carrillos=models.CharField(max_length=50)
	fondodesaco=models.CharField(max_length=50)
	frenillos=models.CharField(max_length=50)
	lenguaTerciomedio=models.CharField(max_length=50)
	paladarDuro=models.CharField(max_length=50)
	paladarBlando=models.CharField(max_length=50)
	istmoBucofaringe=models.CharField(max_length=50)
	lenguaDorso=models.CharField(max_length=50)
	lenguaBordes=models.CharField(max_length=50)
	lenguaVentral=models.CharField(max_length=50)
	pisodelaBoca=models.CharField(max_length=50)
	dientes=models.CharField(max_length=50)
	mucosadelBordealveolar=models.CharField(max_length=50)
	encia=models.CharField(max_length=50)
	sistemaEndocrina=models.CharField(max_length=50)
	gingivitis=models.CharField(max_length=50)
	periodontitis=models.CharField(max_length=50)
	receciongingival=models.CharField(max_length=50)
	bolsasperiodontales=models.CharField(max_length=50)
	movilidadDentario=models.CharField(max_length=50)
	indicedeplaca=models.CharField(max_length=50)
	interpretacionradiografica=models.CharField(max_length=50)
	estudiosdeLaboratorio=models.CharField(max_length=50)
	interpretacionEstudiosLaboratorio=models.CharField(max_length=50)
	

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
 	notas=models.TextField()
 	
 	


CARAS=(
	('S','Cara Superior'),
	('C','Cara Central'),
	('X','Cara Completo'),
	('Z','Cara Izquierda'),
	('D','Cara Derecha'),
	)

class Procedimiento(models.Model):
	pieza=models.IntegerField()
	cara=models.CharField(max_length=4,choices=CARAS)
	tratamiento=models.ForeignKey(ListadeDiagnosticos)





