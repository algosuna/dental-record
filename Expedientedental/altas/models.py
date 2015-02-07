from django.db import models

# Create your models here.

# Modelo de Medicos
class medico(models.Model):
	nombre		= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	apellidoMaterno		= models.CharField(max_length=30)
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
		NombreCompleto = "%s %s"%(self.Nombre,self.Ap_Paterno)
		return NombreCompleto


# Modelo de Pacientes
class paciente(models.Model):
	nombre		= models.CharField(max_length=40)
	apellidPaterno	= models.CharField(max_length=30)
	Ap_Materno		= models.CharField(max_length=30)
	Sexo_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
	Sexo = models.CharField(max_length=2, choices=Sexo_CHOICES)
	Correo_Electronico = models.EmailField(max_length=60)
	Direccion = models.CharField(max_length=70)
	Codigo_Postal = models.IntegerField(max_length=5)
	Estado = models.CharField(max_length=30)
	Ciudad = models.CharField(max_length=30)	
	NSS = models.CharField(max_length=20)
	Telefono = models.CharField(max_length=20)
	NSS = models.CharField(max_length=20)

	def __unicode__(self):
		NombreCompleto = "%s %s %s"%(self.Nombre,self.Ap_Paterno,self.Ap_Materno)
		return NombreCompleto

