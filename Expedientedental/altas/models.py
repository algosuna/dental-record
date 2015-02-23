#encoding: utf-8
from django.db import models
from django.contrib import admin
from precios.models import GrupoPrecios

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
	sex_CHOICES=(

		('M', 'M'),
        ('F', 'F'),
        )
	estado_CHOICES=(

    	('B.C','Baja California'),
    	('CA','California'),

    	)
 	credencialPaciente = models.CharField(max_length=15)
 	grupo= models.ForeignKey(GrupoPrecios)
	nombre	= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	apellidoMaterno	= models.CharField(max_length=30)
	sexo = models.CharField(max_length=2, choices=sex_CHOICES)
	correoElectronico = models.EmailField(max_length=60)
	direccion = models.CharField(max_length=70)
	codigoPostal = models.IntegerField(max_length=5)
	estado = models.CharField(max_length=20 , choices=estado_CHOICES)
	ciudad = models.CharField(max_length=30)	
	nSs = models.CharField(max_length=20)
	telefono = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre+' '+self.apellidoPaterno
