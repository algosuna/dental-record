from django.db import models

# Create your models here.

# Modelo de Medicos
class medico(models.Model):
	Nombre		= models.CharField(max_length=40)
	Ap_Paterno	= models.CharField(max_length=30)
	Ap_Materno		= models.CharField(max_length=30)
	Nombre_Usuario = models.CharField(max_length=30)
	Licencia_Medica = models.CharField(max_length=30)
	Universidad_Egreso= models.CharField(max_length=70)
	RFC = models.CharField(max_length=15)
	Licencia_de_Especialidad = models.CharField(max_length=30)
	Cedula_Estatal = models.CharField(max_length=40)
	Especialidad = models.CharField(max_length=40)
	Telefono = models.CharField(max_length=20)
	Correo_Electronico = models.EmailField(max_length=50)
	Direccion = models.CharField(max_length=70)
	Codigo_Postal = models.IntegerField(max_length=5)
	Estado = models.CharField(max_length=30)
	Ciudad = models.CharField(max_length=30)

	def __unicode__(self):
		NombreCompleto = "%s %s"%(self.Nombre,self.Ap_Paterno)
		return NombreCompleto


# Modelo de Pacientes
class paciente(models.Model):
	Nombre		= models.CharField(max_length=40)
	Ap_Paterno	= models.CharField(max_length=30)
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

