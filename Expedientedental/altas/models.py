from django.db import models

# Create your models here.

# Modelo de Medicos
class medico(models.Model):
	nombre		= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	apellidoMaterno		= models.CharField(max_length=30)
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

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.Nombre,self.Ap_Paterno)
		return nombreCompleto


# Modelo de Pacientes
class paciente(models.Model):
 	credencial_paciente = models.CharField(max_length=15)
	nombre		= models.CharField(max_length=40)
	apellidoPaterno	= models.CharField(max_length=30)
	ApellidoMaterno		= models.CharField(max_length=30)
	sexoopciones=(
        ('M', 'M'),
        ('F', 'F'),
    )
	sexo = models.CharField(max_length=2, choices=sexoopciones)
	correo_Electronico = models.EmailField(max_length=60)
	direccion = models.CharField(max_length=70)
	codigo_Postal = models.IntegerField(max_length=5)
	estado = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)	
	nSs= models.CharField(max_length=20)
	telefono = models.CharField(max_length=20)
	

	def __unicode__(self):
		nmbreCompleto = "%s %s %s"%(self.Nombre,self.Ap_Paterno,self.Ap_Materno)
		return NombreCompleto

