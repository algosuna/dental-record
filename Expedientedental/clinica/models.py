from django.db import models

from altas.models import Medico, Paciente, Evaluacion, Tratamiento,\
    TratamientoPreventivo
from core.models import TimeStampedModel


class Interrogatorio(models.Model):
    BOOLEAN_CHOICES = (
        ('si', 'Si'),
        ('no', 'No')
    )
    ANTECEDENTES_CHOICES = (
        ('tabaco', 'Tabaco'),
        ('alcohol', 'Alcohol'),
        ('ninguna', 'Ninguna')
    )
    CABEZA_CHOICES = (
        ('exotosis', 'Exotosis'),
        ('endostosis', 'Endostosis'),
    )
    CRANEO_CHOICES = (
        ('dolicocefalico', 'Dolicocefalico'),
        ('mesocefalico', 'Mesocefalico'),
    )
    CARA_CHOICES = (
        ('transversales', 'Transversales'),
        ('longitudinales', 'longitudinales'),
    )
    PERFIL_CHOICES = (
        ('concavo', 'Concavo'),
        ('convexo', 'Convexo'),
        ('recto', 'Recto'),
    )
    PIEL_CHOICES = (
        ('normal', 'Normal'),
        ('palida', 'Palida'),
        ('cianotica', 'Cianotica'),
        ('enrojecida', 'Enrojecida'),
    )
    GRUPOSANGUINEO_CHOICES = (
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    )
    paciente = models.ForeignKey(Paciente)
    medico = models.ForeignKey(Medico)
    credencialPaciente = models.CharField(max_length=15, null=True)
    herenciaMadre = models.CharField(max_length=200)
    herenciaPadre = models.CharField(max_length=200)
    herenciaHermanos = models.CharField(max_length=200)
    herenciaHijos = models.CharField(max_length=200)
    herenciaEsposos = models.CharField(max_length=200, blank=True)
    herenciaTios = models.CharField(max_length=200, blank=True)
    herenciaAbuelos = models.CharField(max_length=200, blank=True)
    eInflamatoriasnotopciones = models.CharField(max_length=200, blank=True)
    ets = models.CharField(max_length=200, blank=True)
    eDegenerativas = models.CharField(max_length=200, blank=True)
    eNeoplasticas = models.CharField(max_length=200, blank=True)
    eCongenitas = models.CharField(max_length=200, blank=True)
    otras = models.CharField(max_length=200, blank=True)
    habitosHigienicosVest = models.CharField(max_length=200)
    habitosHigienicosCorp = models.CharField(max_length=200)
    frecuenciaLavadoDental = models.CharField(max_length=200, blank=True)
    uxiliaresBucales = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    consumodeGolosinas = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    gruposanguineo = models.CharField(
        max_length=20, choices=GRUPOSANGUINEO_CHOICES, blank=True)
    factorRh = models.CharField(max_length=50, blank=True)
    cartilladeVacunacion = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    esquemaCompleto = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    esquemaFalta = models.CharField(max_length=200, blank=True)
    adicciones = models.CharField(max_length=15, choices=ANTECEDENTES_CHOICES)
    alergias = models.CharField(max_length=400)
    fechaHospitalizaion = models.CharField(max_length=400)
    motivo = models.CharField(max_length=400, blank=True)
    padecimientoActual = models.CharField(max_length=500)
    aparatoDigestivo = models.CharField(max_length=200)
    aparatoRespiratorio = models.CharField(max_length=200)
    aparatoCardioBascular = models.CharField(max_length=200)
    apararoGenitourinario = models.CharField(max_length=200)
    sistemaEndocrina = models.CharField(max_length=200)
    sistemaHemopoyetico = models.CharField(max_length=200)
    sistemamusculoEsqueletico = models.CharField(max_length=200)
    aparatoTegumentario = models.CharField(max_length=200)
    habitusExterior = models.CharField(max_length=500)
    peso = models.CharField(max_length=10, blank=True)
    talla = models.CharField(max_length=10, blank=True)
    complexion = models.CharField(max_length=100, blank=True)
    frecuenciaCardiaca = models.CharField(max_length=100, blank=True)
    tensionarterial = models.CharField(max_length=100, blank=True)
    frecuenciaRespiratoria = models.CharField(max_length=100, blank=True)
    temperatura = models.CharField(max_length=60, blank=True)
    cabeza = models.CharField(
        max_length=400, choices=CABEZA_CHOICES, blank=True)
    craneo = models.CharField(
        max_length=50, choices=CRANEO_CHOICES, blank=True)
    caraAsimetria = models.CharField(
        max_length=50, choices=CARA_CHOICES, blank=True)
    perfil = models.CharField(
        max_length=15, choices=PERFIL_CHOICES, blank=True)
    piel = models.CharField(max_length=50, choices=PIEL_CHOICES, blank=True)
    musculos = models.CharField(max_length=500, blank=True)
    cuello = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    otros = models.CharField(max_length=200, blank=True)
    ruidos = models.CharField(max_length=200, blank=True)
    chasquidos = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    crepitacion = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    difparaAbrirlaboca = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    dolorabertura = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    fatigadolormuscular = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    disminuciondelaavertura = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    desviacionaverturadecierre = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    ganglios = models.CharField(max_length=200, blank=True)
    glandulassalivales = models.CharField(max_length=200, blank=True)
    labioExterno = models.CharField(max_length=200, blank=True)
    bordebermellon = models.CharField(max_length=200, blank=True)
    labiointerno = models.CharField(max_length=200, blank=True)
    Comisuras = models.CharField(max_length=200, blank=True)
    carrillos = models.CharField(max_length=200, blank=True)
    fondodesaco = models.CharField(max_length=200, blank=True)
    frenillos = models.CharField(max_length=200, blank=True)
    lenguaTerciomedio = models.CharField(max_length=200, blank=True)
    paladarDuro = models.CharField(max_length=200, blank=True)
    paladarBlando = models.CharField(max_length=200, blank=True)
    istmoBucofaringe = models.CharField(max_length=200, blank=True)
    lenguaDorso = models.CharField(max_length=200, blank=True)
    lenguaBordes = models.CharField(max_length=200, blank=True)
    lenguaVentral = models.CharField(max_length=200, blank=True)
    pisodelaBoca = models.CharField(max_length=200, blank=True)
    dientes = models.CharField(max_length=200, blank=True)
    mucosadelBordealveolar = models.CharField(max_length=200, blank=True)
    encia = models.CharField(max_length=200, blank=True)
    gingivitis = models.CharField(max_length=100, blank=True)
    periodontitis = models.CharField(max_length=100, blank=True)
    receciongingival = models.CharField(max_length=100, blank=True)
    bolsasperiodontales = models.CharField(max_length=100, blank=True)
    movilidadDentario = models.CharField(max_length=100, blank=True)
    indicedeplaca = models.CharField(max_length=100, blank=True)
    interpretacionradiografica = models.CharField(max_length=100, blank=True)
    estudiosdeLaboratorio = models.CharField(max_length=100, blank=True)
    interpretacionEstudiosLaboratorio = models.CharField(
        max_length=100, blank=True)

    def __unicode__(self):

        nombres = "%s %s" % (self.medico, self.paciente)
        return nombres


class Odontograma(TimeStampedModel):
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    notas = models.TextField()
    evaluacion = models.ForeignKey(Evaluacion)
    tratamiento_preventivo = models.ForeignKey(
        TratamientoPreventivo, blank=True, null=True)

    def __unicode__(self):
        odontograma = '%s %s' % (self.id, self.evaluacion)
        return odontograma


class Procedimiento(models.Model):
    CARAS_CHOICES = (
        ('S', 'Vestibular'),
        ('C', 'Oclusal'),
        ('X', 'Pieza Completa'),
        ('Z', 'Distal'),
        ('D', 'Mesial'),
        ('I', 'Palatino'),
    )
    STATUS_CHOICES = (
        ('recomendado', 'Recomendado'),
        ('autorizado', 'Autorizado'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado')
    )

    pieza = models.IntegerField()
    cara = models.CharField(max_length=4, choices=CARAS_CHOICES)
    tratamiento = models.ForeignKey(Tratamiento)
    odontograma = models.ForeignKey(Odontograma)
    diagnostico = models.TextField()
    notas = models.TextField(blank=True)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='recomendado')

    def __unicode__(self):
        procedimiento = '%s' % (self.tratamiento)
        return procedimiento


class Bitacora(TimeStampedModel):
    procedimiento = models.ForeignKey(Procedimiento)
    descripcion = models.TextField()

    def __unicode__(self):
        entrada = '%s %s' % (self.id, self.created_at)
        return entrada
