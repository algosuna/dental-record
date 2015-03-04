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
	credencialPaciente = models.CharField(max_length=15, null=True)
	herenciaMadre=models.CharField(max_length=200)
	herenciaPadre=models.CharField(max_length=200)
	herenciaHermanos=models.CharField(max_length=200)
	herenciaHijos=models.CharField(max_length=200)
	herenciaEsposos=models.CharField(max_length=200)
	herenciaTios=models.CharField(max_length=200)
	herenciaAbuelos=models.CharField(max_length=200)
	eInflamatoriasnotopciones=models.CharField(max_length=200)
	ets=models.CharField(max_length=200)
	eDegenerativas=models.CharField(max_length=200)
	eNeoplasticas=models.CharField(max_length=200)
	eCongenitas=models.CharField(max_length=200)
	otras=models.CharField(max_length=200)
	habitosHigienicosVest=models.CharField(max_length=200)
	habitosHigienicosCorp=models.CharField(max_length=200)
	frecuenciaLavadoDental=models.CharField(max_length=200)
	uxiliaresBucales=models.CharField(max_length=2,choices=auxBucal_CHOICES)
	consumodeGolosinas=models.CharField(max_length=2,choices=chatarra_CHOICES)
	gruposanguineo=models.CharField(max_length=20,choices=grupoSanguineo_CHOICES)
	factorRh=models.CharField(max_length=50)
	cartilladeVacunacion=models.CharField(max_length=2,choices=cartilla_CHOICES)
	esquemaCompleto=models.CharField(max_length=2,choices=esquema_Choices)
	esquemaFalta=models.CharField(max_length=200)
	adicciones=models.CharField(max_length=15,choices=antecedentes_Choices)
	alergias=models.CharField(max_length=400,choices=alergias_CHOICES)
	fechaHospitalizaion=models.CharField(max_length=400)
	motivo=models.CharField(max_length=400)
	padecimientoActual=models.CharField(max_length=500)
	aparatoDigestivo=models.CharField(max_length=200)
	aparatoRespiratorio=models.CharField(max_length=200)
	aparatoCardioBascular=models.CharField(max_length=200)
	apararoGenitourinario=models.CharField(max_length=200)
	sistemaEndocrina=models.CharField(max_length=200)
	sistemaHemopoyetico=models.CharField(max_length=200)
	sistemamusculoEsqueletico=models.CharField(max_length=200)
	aparatoTegumentario=models.CharField(max_length=200)
	habitusExterior=models.CharField(max_length=500)
	peso=models.CharField(max_length=10)
	talla=models.CharField(max_length=10)
	complexion=models.CharField(max_length=100)
	frecuenciaCardiaca= models.CharField(max_length=100)
	tensionarterial=models.CharField(max_length=100)
	frecuenciaRespiratoria=models.CharField(max_length=100)
	temperatura=models.CharField(max_length=60)
	cabeza=models.CharField(max_length=400,choices=cabeza_CHOICES)
	craneo=models.CharField(max_length=50,choices=craneo_CHOICES)
	caraAsimetria=models.CharField(max_length=50,choices=cara_CHOICES)
	perfil= models.CharField(max_length=15,choices=perfil_CHOICES)
	piel=models.CharField(max_length=50,choices=piel_CHOICES)
	musculos=models.CharField(max_length=500)
	cuello=models.CharField(max_length=15,choices=cuello_CHOICES)
	otros=models.CharField(max_length=200)
	ruidos=models.CharField(max_length=200)
	chasquidos=models.CharField(max_length=15,choices=chasquidos_CHOICES)
	crepitacion=models.CharField(max_length=15,choices=crepitacion_CHOICES)
	difparaAbrirlaboca=models.CharField(max_length=15,choices=dificultadParaAbrirLaBoca_CHOICES)
	dolorabertura=models.CharField(max_length=15,choices=dolorabertura_CHOICES)
	fatigadolormuscular=models.CharField(max_length=15,choices=fatigadolormuscular_CHOICES)
	disminuciondelaavertura=models.CharField(max_length=10,choices=disminuciondelaavertura_CHOICES)
	desviacionaverturadecierre=models.CharField(max_length=10,choices=desviacionaverturadecierre_CHOICES)
	ganglios=models.CharField(max_length=200)
	glandulassalivales=models.CharField(max_length=200)
	labioExterno=models.CharField(max_length=200)
	bordebermellon=models.CharField(max_length=200)
	labiointerno=models.CharField(max_length=200)
	Comisuras=models.CharField(max_length=200)
	carrillos=models.CharField(max_length=200)
	fondodesaco=models.CharField(max_length=200)
	frenillos=models.CharField(max_length=200)
	lenguaTerciomedio=models.CharField(max_length=200)
	paladarDuro=models.CharField(max_length=200)
	paladarBlando=models.CharField(max_length=200)
	istmoBucofaringe=models.CharField(max_length=200)
	lenguaDorso=models.CharField(max_length=200)
	lenguaBordes=models.CharField(max_length=200)
	lenguaVentral=models.CharField(max_length=200)
	pisodelaBoca=models.CharField(max_length=200)
	dientes=models.CharField(max_length=200)
	mucosadelBordealveolar=models.CharField(max_length=200)
	encia=models.CharField(max_length=200)
	gingivitis=models.CharField(max_length=100)
	periodontitis=models.CharField(max_length=100)
	receciongingival=models.CharField(max_length=100)
	bolsasperiodontales=models.CharField(max_length=100)
	movilidadDentario=models.CharField(max_length=100)
	indicedeplaca=models.CharField(max_length=100)
	interpretacionradiografica=models.CharField(max_length=100)
	estudiosdeLaboratorio=models.CharField(max_length=100)
	interpretacionEstudiosLaboratorio=models.CharField(max_length=100)
	

	def __unicode__(self):

		nombres ="%s %s"% (self.medico,self.paciente)
		return nombres


class ListadeDiagnosticos(models.Model):
	codigoDiagnostico=models.CharField(max_length=15)
	nombreDiagnostico=models.CharField(max_length=30)
	
	def __unicode__(self):
		codigoCie="%s  %s"%(self.codigoDiagnostico,self.nombreDiagnostico)
		return codigoCie

class Odontograma(models.Model):
 	doctor = models.ForeignKey(Medico, null=True)
 	paciente = models.ForeignKey(Paciente, null=True)
 	fechayHora = models.DateTimeField(auto_now_add=True)
 	notas = models.TextField()
 	
 	



class Procedimiento(models.Model):
	CARAS_CHOICES = (
		('S','Cara Superior'),
		('C','Cara Central'),
		('X','Cara Completo'),
		('Z','Cara Izquierda'),
		('D','Cara Derecha'),
	)

	pieza = models.IntegerField()
	cara = models.CharField(max_length=4, choices=CARAS_CHOICES)
	tratamiento = models.CharField(max_length=300, null=True)





class TablaPrueba(models.Model):
	sex_CHOICES=(

		('M', 'M'),
        ('F', 'F'),
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
	#exploracion
	cabeza_CHOICES=(
		('Exotosis', 'Exotosis'),
        ('Endostosis', 'Endostosis'),        
        )

	nombre	= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	apellidoMaterno	= models.CharField(max_length=30)
	credencialPaciente = models.CharField(max_length=15)
	sexo = models.CharField(max_length=2, choices=sex_CHOICES)
	ocupacion	= models.CharField(max_length=30)
	escolaridad	= models.CharField(max_length=30)
	estadoCivil	= models.CharField(max_length=30)
	herenciaMadre=models.CharField(max_length=50)
	herenciaPadre=models.CharField(max_length=50)
	herenciaHermanos=models.CharField(max_length=50)
	herenciaHijos=models.CharField(max_length=50)
	habitosHigienicosVest=models.CharField(max_length=50)
	habitosHigienicosCorp=models.CharField(max_length=50)
	adicciones=models.CharField(max_length=15,choices=antecedentes_Choices)
	alergias=models.CharField(max_length=400,choices=alergias_CHOICES)
	fechaHospitalizaion=models.CharField(max_length=400)
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
	cabeza=models.CharField(max_length=40,choices=cabeza_CHOICES)	

	def __unicode__(self):

		nombres ="%s"% (self.nombre)
		return nombres
