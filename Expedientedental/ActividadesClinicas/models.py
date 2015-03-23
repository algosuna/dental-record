from django.db import models

from altas.models import Medico, Paciente

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

	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
	credencialPaciente = models.CharField(max_length=15, null=True)
	herenciaMadre=models.CharField(max_length=200)
	herenciaPadre=models.CharField(max_length=200)
	herenciaHermanos=models.CharField(max_length=200)
	herenciaHijos=models.CharField(max_length=200)
	herenciaEsposos=models.CharField(max_length=200, blank=True)
	herenciaTios=models.CharField(max_length=200, blank=True)
	herenciaAbuelos=models.CharField(max_length=200, blank=True)
	eInflamatoriasnotopciones=models.CharField(max_length=200, blank=True)
	ets=models.CharField(max_length=200, blank=True)
	eDegenerativas=models.CharField(max_length=200, blank=True)
	eNeoplasticas=models.CharField(max_length=200, blank=True)
	eCongenitas=models.CharField(max_length=200, blank=True)
	otras=models.CharField(max_length=200, blank=True)
	habitosHigienicosVest=models.CharField(max_length=200)
	habitosHigienicosCorp=models.CharField(max_length=200)
	frecuenciaLavadoDental=models.CharField(max_length=200, blank=True)
	uxiliaresBucales=models.CharField(max_length=2,choices=auxBucal_CHOICES, blank=True)
	consumodeGolosinas=models.CharField(max_length=2,choices=chatarra_CHOICES, blank=True)
	gruposanguineo=models.CharField(max_length=20,choices=grupoSanguineo_CHOICES, blank=True)
	factorRh=models.CharField(max_length=50, blank=True)
	cartilladeVacunacion=models.CharField(max_length=2,choices=cartilla_CHOICES, blank=True)
	esquemaCompleto=models.CharField(max_length=2,choices=esquema_Choices, blank=True)
	esquemaFalta=models.CharField(max_length=200, blank=True)
	adicciones=models.CharField(max_length=15,choices=antecedentes_Choices)
	alergias=models.CharField(max_length=400)
	fechaHospitalizaion=models.CharField(max_length=400)
	motivo=models.CharField(max_length=400, blank=True)
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
	peso=models.CharField(max_length=10, blank=True)
	talla=models.CharField(max_length=10, blank=True)
	complexion=models.CharField(max_length=100, blank=True)
	frecuenciaCardiaca= models.CharField(max_length=100, blank=True)
	tensionarterial=models.CharField(max_length=100, blank=True)
	frecuenciaRespiratoria=models.CharField(max_length=100, blank=True)
	temperatura=models.CharField(max_length=60, blank=True)
	cabeza=models.CharField(max_length=400,choices=cabeza_CHOICES, blank=True)
	craneo=models.CharField(max_length=50,choices=craneo_CHOICES, blank=True)
	caraAsimetria=models.CharField(max_length=50,choices=cara_CHOICES, blank=True)
	perfil= models.CharField(max_length=15,choices=perfil_CHOICES, blank=True)
	piel=models.CharField(max_length=50,choices=piel_CHOICES, blank=True)
	musculos=models.CharField(max_length=500, blank=True)
	cuello=models.CharField(max_length=15,choices=cuello_CHOICES, blank=True)
	otros=models.CharField(max_length=200, blank=True)
	ruidos=models.CharField(max_length=200, blank=True)
	chasquidos=models.CharField(max_length=15,choices=chasquidos_CHOICES, blank=True)
	crepitacion=models.CharField(max_length=15,choices=crepitacion_CHOICES, blank=True)
	difparaAbrirlaboca=models.CharField(max_length=15,choices=dificultadParaAbrirLaBoca_CHOICES, blank=True)
	dolorabertura=models.CharField(max_length=15,choices=dolorabertura_CHOICES, blank=True)
	fatigadolormuscular=models.CharField(max_length=15,choices=fatigadolormuscular_CHOICES, blank=True)
	disminuciondelaavertura=models.CharField(max_length=10,choices=disminuciondelaavertura_CHOICES, blank=True)
	desviacionaverturadecierre=models.CharField(max_length=10,choices=desviacionaverturadecierre_CHOICES, blank=True)
	ganglios=models.CharField(max_length=200, blank=True)
	glandulassalivales=models.CharField(max_length=200, blank=True)
	labioExterno=models.CharField(max_length=200, blank=True)
	bordebermellon=models.CharField(max_length=200, blank=True)
	labiointerno=models.CharField(max_length=200, blank=True)
	Comisuras=models.CharField(max_length=200, blank=True)
	carrillos=models.CharField(max_length=200, blank=True)
	fondodesaco=models.CharField(max_length=200, blank=True)
	frenillos=models.CharField(max_length=200, blank=True)
	lenguaTerciomedio=models.CharField(max_length=200, blank=True)
	paladarDuro=models.CharField(max_length=200, blank=True)
	paladarBlando=models.CharField(max_length=200, blank=True)
	istmoBucofaringe=models.CharField(max_length=200, blank=True)
	lenguaDorso=models.CharField(max_length=200, blank=True)
	lenguaBordes=models.CharField(max_length=200, blank=True)
	lenguaVentral=models.CharField(max_length=200, blank=True)
	pisodelaBoca=models.CharField(max_length=200, blank=True)
	dientes=models.CharField(max_length=200, blank=True)
	mucosadelBordealveolar=models.CharField(max_length=200, blank=True)
	encia=models.CharField(max_length=200, blank=True)
	gingivitis=models.CharField(max_length=100, blank=True)
	periodontitis=models.CharField(max_length=100, blank=True)
	receciongingival=models.CharField(max_length=100, blank=True)
	bolsasperiodontales=models.CharField(max_length=100, blank=True)
	movilidadDentario=models.CharField(max_length=100, blank=True)
	indicedeplaca=models.CharField(max_length=100, blank=True)
	interpretacionradiografica=models.CharField(max_length=100, blank=True)
	estudiosdeLaboratorio=models.CharField(max_length=100, blank=True)
	interpretacionEstudiosLaboratorio=models.CharField(max_length=100, blank=True)

	def __unicode__(self):

		nombres ="%s %s"% (self.medico,self.paciente)
		return nombres

class Odontograma(models.Model):
 	doctor = models.ForeignKey(Medico, null=True)
 	paciente = models.ForeignKey(Paciente, null=True)
 	fechayHora = models.DateTimeField(auto_now_add=True)
 	notas = models.TextField()

class Tratamiento(models.Model):
	codigoTratamiento = models.CharField(max_length=15)
	nombreTratamiento = models.CharField(max_length=150)



	def __unicode__(self):
		tratamiento = '%s %s'%(self.codigoTratamiento, self.nombreTratamiento)
		return tratamiento

class Procedimiento(models.Model):
	CARAS_CHOICES = (
		('S', 'Vestibular'),
		('C', 'Oclusal'),
		('X', 'Pieza Completa'),
		('Z', 'Distal'),
		('D', 'Mesial'),
		('I', 'Palatino'),
	)

	pieza = models.IntegerField(null=True, default='X')
	cara = models.CharField(max_length=4, choices=CARAS_CHOICES)
	tratamiento = models.ForeignKey(Tratamiento, null=True)
	odontograma = models.ForeignKey(Odontograma, null=True)
