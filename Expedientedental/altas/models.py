# encoding: utf-8
from os.path import splitext
from django.db import models
from django.contrib.auth.models import User


class Grupo(models.Model):
    '''The name and number which a patient belongs to.'''
    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)

    def __unicode__(self):
        grupo = '%s - %s' % (self.numero, self.nombre)
        return grupo


class Medico(models.Model):
    user = models.ForeignKey(User, unique=True)
    mothers_last_name = models.CharField(max_length=30, blank=True)
    universidad_egreso = models.CharField(max_length=70)
    licencia_medica = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=40)
    licencia_especialidad = models.CharField(max_length=30)
    cedula_estatal = models.CharField(max_length=40)
    rfc = models.CharField(max_length=15)
    direccion = models.CharField(max_length=70)
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    codigo_postal = models.IntegerField(max_length=5)
    telefono = models.CharField(max_length=20)

    def __unicode__(self):
        nombre = '%s' % (self.user)
        return nombre


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
    apellidoMaterno = models.CharField(max_length=30)
    sexo = models.CharField(max_length=2, choices=SEX_CHOICES)
    correoElectronico = models.EmailField(max_length=60)
    direccion = models.CharField(max_length=70)
    codigoPostal = models.IntegerField(max_length=5)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    ciudad = models.CharField(max_length=30)
    nSs = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

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
    pass


class TratamientoPreventivo(Metodo):
    pass


class Tratamiento(Metodo):
    pass
