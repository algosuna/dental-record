# encoding: utf-8
from os.path import splitext

from django.db import models
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords


class Grupo(models.Model):
    '''The name and number which a patient belongs to.'''
    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)

    history = HistoricalRecords()

    def __unicode__(self):
        grupo = '%s - %s' % (self.numero, self.nombre)
        return grupo


class Medico(models.Model):
    user = models.ForeignKey(User, unique=True)
    mothers_last_name = models.CharField(max_length=30)
    universidad_egreso = models.CharField(max_length=70, blank=True)
    licencia_medica = models.CharField(max_length=30, blank=True)
    especialidad = models.CharField(max_length=40, blank=True)
    licencia_especialidad = models.CharField(max_length=30, blank=True)
    cedula_estatal = models.CharField(max_length=40, blank=True)
    rfc = models.CharField(max_length=15)
    direccion = models.CharField(max_length=70, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=30, blank=True)
    codigo_postal = models.IntegerField(max_length=5, null=True, blank=True)
    telefono = models.CharField(max_length=20)

    history = HistoricalRecords()

    def __unicode__(self):
        return unicode(self.user.get_full_name())


class Paciente(models.Model):

    def imagen_url(self, filename):
        name, ext = splitext(filename)
        url = 'pacientes/%s%s' % (self.nombre, ext)
        return url

    SEX_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    )
    ESTADO_CHOICES = (
        ('bc', 'Baja California'),
        ('ca', 'California'),
    )

    credencialPaciente = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to=imagen_url, null=True, blank=True)
    grupo = models.ForeignKey(Grupo)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30, blank=True)
    sexo = models.CharField(max_length=2, choices=SEX_CHOICES)
    correoElectronico = models.EmailField(max_length=60, blank=True)
    direccion = models.CharField(max_length=70, blank=True)
    codigoPostal = models.IntegerField(max_length=5, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES,
                              blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    nSs = models.CharField(max_length=20, blank=True)
    telefono = models.CharField(max_length=20)

    history = HistoricalRecords()

    def nombre_completo(self):
        nombreCompleto = '%s %s %s' % (
            self.nombre, self.apellidoPaterno, self.apellidoMaterno)
        return nombreCompleto

    def imagen_nombre(self):
        nombre = '%s-%s' % (self.apellidoPaterno, self.nombre)
        return nombre

    def __unicode__(self):
        return self.nombre_completo()


class Metodo(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __unicode__(self):
        str_ = '%s - %s' % (self.codigo, self.nombre)
        return str_


class Evaluacion(Metodo):
    history = HistoricalRecords()


class TratamientoPreventivo(Metodo):
    history = HistoricalRecords()


class Tratamiento(Metodo):
    history = HistoricalRecords()
