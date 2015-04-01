# encoding: utf-8
from os.path import splitext
from django.db import models


class Grupo(models.Model):
    """The name and number which a patient belongs to."""

    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)

    def __unicode__(self):
        grupo = "%s - %s" % (self.numero, self.nombre)
        return grupo


class Medico(models.Model):

    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    nombreUsuario = models.CharField(max_length=30)
    licenciaMedica = models.CharField(max_length=30)
    universidadEgreso = models.CharField(max_length=70)
    rfc = models.CharField(max_length=15)
    licenciaDeEspecialidad = models.CharField(max_length=30)
    cedulaEstatal = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)
    correoElectronico = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=70)
    codigoPostal = models.IntegerField(max_length=5)
    estado = models.CharField(max_length=30)
    Ciudad = models.CharField(max_length=30)

    def __unicode__(self):
        nombreCompleto = "%s %s %s" % (
            self.nombre, self.apellidoPaterno, self.apellidoMaterno)
        return nombreCompleto


class Paciente(models.Model):

    def imagen_url(self, filename):
        name, ext = splitext(filename)
        url = 'Pacientes/%s%s' % (self.nombre_imagen, ext)
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
        nombreCompleto = "%s %s %s" % (
            self.nombre, self.apellidoPaterno, self.apellidoMaterno)
        return nombreCompleto

    def imagen_nombre(self):
        nombre = "%s-%s" % (self.apellidoPaterno, self.nombre)
        return nombre

    def __unicode__(self):
        return self.nombre_completo()


class Evaluacion(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        evaluacion = '%s - %s' % (self.codigo, self.nombre)
        return evaluacion


class TratamientoPreventivo(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        tratamiento_preventivo = '%s %s' % (self.codigo, self.nombre)
        return tratamiento_preventivo


class Tratamiento(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        tratamiento = '%s %s' % (self.codigo, self.nombre)
        return tratamiento
