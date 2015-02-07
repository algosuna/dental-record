from django.db import models

# Create your models here.

# Modelo de Medicos
class medico(models.Model):
	nombre		= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	apellidoMaterno		= models.CharField(max_length=30)
<<<<<<< HEAD
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
=======
	nombre_Usuario = models.CharField(max_length=30)
	licencia_Medica = models.CharField(max_length=30)
	universidad_Egreso= models.CharField(max_length=70)
	rfc = models.CharField(max_length=15)
	licenciadeEspecialidad = models.CharField(max_length=30)
	cedulaEstatal = models.CharField(max_length=40)
	especialidad = models.CharField(max_length=40)
	telefono = models.CharField(max_length=20)
	correo_Electronico = models.EmailField(max_length=50)
	direccion = models.CharField(max_length=70)
	codigo_Postal = models.IntegerField(max_length=5)
	estado = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
>>>>>>> 231e7e4e8458126819e25bd4e127a40176efd53e

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.Nombre,self.Ap_Paterno)
		return nombreCompleto


# Modelo de Pacientes
class paciente(models.Model):
<<<<<<< HEAD
	nombre		= models.CharField(max_length=40)
	apellidPaterno	= models.CharField(max_length=30)
	Ap_Materno		= models.CharField(max_length=30)
	Sexo_CHOICES = (
=======
 	credencial_paciente = models.CharField(max_length=15)
	nombre		= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	ApellidoMaterno		= models.CharField(max_length=30)
	sexo_CHOICES = (
>>>>>>> 231e7e4e8458126819e25bd4e127a40176efd53e
        ('M', 'M'),
        ('F', 'F'),
    )
	sexo = models.CharField(max_length=2, choices=Sexo_CHOICES)
	correo_Electronico = models.EmailField(max_length=60)
	direccion = models.CharField(max_length=70)
	codigo_Postal = models.IntegerField(max_length=5)
	estado = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)	
	nSS = models.CharField(max_length=20)
	telefono = models.CharField(max_length=20)
	nss models.CharField(max_length=20)

	def __unicode__(self):
		nmbreCompleto = "%s %s %s"%(self.Nombre,self.Ap_Paterno,self.Ap_Materno)
		return NombreCompleto

