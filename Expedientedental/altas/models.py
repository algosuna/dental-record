#encoding: utf-8
from django.db import models
from django.contrib import admin

# Create your models here.

# Modelo de Medicos
class Medico(models.Model):
	nombre	= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	apellidoMaterno	= models.CharField(max_length=30)
	nombreUsuario = models.CharField(max_length=30)
	licenciaMedica = models.CharField(max_length=30)
	universidadEgreso= models.CharField(max_length=70)
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
		nombreCompleto = "%s %s"%(self.nombre,self.apellidoPaterno)
		return nombreCompleto


# Modelo de Pacientes

class Paciente(models.Model):
 	credencialPaciente = models.CharField("Credencial de Paciente",max_length=15)
	nombre	= models.CharField("Nombre",max_length=40)
	apellidoPaterno	= models.CharField("Apellido Paterno",max_length=30)
	apellidoMaterno	= models.CharField("Apellido Materno",max_length=30)
	sexoopciones=(

        ('M', 'M'),
        ('F', 'F'),
    )
	sexo = models.CharField("Sexo",max_length=2, choices=sexoopciones)
	correoElectronico = models.EmailField("Correo E",max_length=60)
	direccion = models.CharField("Direccion",max_length=70)
	codigoPostal = models.IntegerField("Codigo Postal",max_length=5)
	estado = models.CharField("Estado",max_length=30)
	ciudad = models.CharField("Ciudad",max_length=30)	
	nSs = models.CharField("NSS",max_length=20)
	telefono = models.CharField("Telefono",max_length=20)

	def __unicode__(self):
		return self.nombre+' '+self.apellidoPaterno
