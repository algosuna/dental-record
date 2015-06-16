from os.path import splitext

from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField
from simple_history.models import HistoricalRecords
from core.models import TimeStampedModel

from altas.models import (
    Medico, Paciente, Evaluacion, Tratamiento, TratamientoPreventivo
)


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
    credencial_paciente = models.CharField(max_length=15, null=True)
    herencia_madre = models.CharField(max_length=200)
    herencia_padre = models.CharField(max_length=200)
    herencia_hermanos = models.CharField(max_length=200)
    herencia_hijos = models.CharField(max_length=200)
    herencia_esposos = models.CharField(max_length=200, blank=True)
    herencia_tios = models.CharField(max_length=200, blank=True)
    herencia_abuelos = models.CharField(max_length=200, blank=True)
    e_inflamatorias_not_opciones = models.CharField(max_length=200, blank=True)
    ets = models.CharField(max_length=200, blank=True)
    e_degenerativas = models.CharField(max_length=200, blank=True)
    e_neoplasticas = models.CharField(max_length=200, blank=True)
    e_congenitas = models.CharField(max_length=200, blank=True)
    otras = models.CharField(max_length=200, blank=True)
    habitos_higienicosVest = models.CharField(max_length=200)
    habitos_higienicos_corp = models.CharField(max_length=200)
    frecuencia_lavado_dental = models.CharField(max_length=200, blank=True)
    auxiliares_bucales = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    consumo_de_golosinas = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    grupo_sanguineo = models.CharField(
        max_length=20, choices=GRUPOSANGUINEO_CHOICES, blank=True)
    factor_rh = models.CharField(max_length=50, blank=True)
    cartilla_de_vacunacion = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    esquema_completo = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    esquema_falta = models.CharField(max_length=200, blank=True)
    adicciones = models.CharField(max_length=15, choices=ANTECEDENTES_CHOICES)
    alergias = models.CharField(max_length=400)
    fecha_hospitalizaion = models.CharField(max_length=400)
    motivo = models.CharField(max_length=400, blank=True)
    padecimiento_actual = models.CharField(max_length=500)
    aparato_digestivo = models.CharField(max_length=200)
    aparato_respiratorio = models.CharField(max_length=200)
    aparato_cardioBascular = models.CharField(max_length=200)
    aparato_genitourinario = models.CharField(max_length=200)
    sistema_endocrina = models.CharField(max_length=200)
    sistema_hemopoyetico = models.CharField(max_length=200)
    sistema_musculoEsqueletico = models.CharField(max_length=200)
    aparato_tegumentario = models.CharField(max_length=200)
    habitus_exterior = models.CharField(max_length=500)
    peso = models.CharField(max_length=10, blank=True)
    talla = models.CharField(max_length=10, blank=True)
    complexion = models.CharField(max_length=100, blank=True)
    frecuencia_cardiaca = models.CharField(max_length=100, blank=True)
    tension_arterial = models.CharField(max_length=100, blank=True)
    frecuencia_respiratoria = models.CharField(max_length=100, blank=True)
    temperatura = models.CharField(max_length=60, blank=True)
    cabeza = models.CharField(
        max_length=400, choices=CABEZA_CHOICES, blank=True)
    craneo = models.CharField(
        max_length=50, choices=CRANEO_CHOICES, blank=True)
    cara_asimetria = models.CharField(
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
    dif_para_abrir_la_boca = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    dolor_abertura = models.CharField(max_length=2, choices=BOOLEAN_CHOICES)
    fatiga_dolor_muscular = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    disminucion_de_la_avertura = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    desviacion_avertura_de_cierre = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES)
    ganglios = models.CharField(max_length=200, blank=True)
    glandulas_salivales = models.CharField(max_length=200, blank=True)
    labio_externo = models.CharField(max_length=200, blank=True)
    borde_bermellon = models.CharField(max_length=200, blank=True)
    labio_interno = models.CharField(max_length=200, blank=True)
    comisuras = models.CharField(max_length=200, blank=True)
    carrillos = models.CharField(max_length=200, blank=True)
    fondo_de_saco = models.CharField(max_length=200, blank=True)
    frenillos = models.CharField(max_length=200, blank=True)
    lengua_tercio_medio = models.CharField(max_length=200, blank=True)
    paladar_duro = models.CharField(max_length=200, blank=True)
    paladar_blando = models.CharField(max_length=200, blank=True)
    istmo_bucofaringe = models.CharField(max_length=200, blank=True)
    lengua_dorso = models.CharField(max_length=200, blank=True)
    lengua_bordes = models.CharField(max_length=200, blank=True)
    lengua_ventral = models.CharField(max_length=200, blank=True)
    piso_de_la_boca = models.CharField(max_length=200, blank=True)
    dientes = models.CharField(max_length=200, blank=True)
    mucosa_del_borde_alveolar = models.CharField(max_length=200, blank=True)
    encia = models.CharField(max_length=200, blank=True)
    gingivitis = models.CharField(max_length=100, blank=True)
    periodontitis = models.CharField(max_length=100, blank=True)
    rececion_gingival = models.CharField(max_length=100, blank=True)
    bolsas_periodontales = models.CharField(max_length=100, blank=True)
    movilidad_dentario = models.CharField(max_length=100, blank=True)
    indice_de_placa = models.CharField(max_length=100, blank=True)
    interpretacion_radiografica = models.CharField(max_length=100, blank=True)
    estudios_de_laboratorio = models.CharField(max_length=100, blank=True)
    interpretacion_estudios_laboratorio = models.CharField(
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
        return unicode(self.tratamiento)


class Bitacora(TimeStampedModel):
    procedimiento = models.ForeignKey(Procedimiento)
    titulo = models.CharField(max_length=140)
    descripcion = models.TextField()

    def __unicode__(self):
        entrada = '%s %s' % (self.id, self.created_at)
        return entrada


class Radiografia(TimeStampedModel):

    def url(self, filename):
        name, ext = splitext(filename)
        url = 'radiografia/%s%s' % (self.title. ext)
        return url

    paciente = models.ForeignKey(Paciente)
    image = ThumbnailerImageField(upload_to='radiografia')
    title = models.CharField(max_length=80)
    description = models.TextField()

    history = HistoricalRecords()

    def __unicode__(self):
        return '%s - %s' % (self.title, self.paciente)
