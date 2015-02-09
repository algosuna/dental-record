from django.db import models

# Create your models here.

# Modelo de Precios de Servicios

class PrecioServicio(models.Model):
	nombreDelServicio	= models.CharField(max_length=50,unique = True)
	
	def __unicode__(self):
		Servicio = "%s"%(self.nombreDelServicio)
		return Servicio


# Modelo de Grupo de Precios. 
# Aqui se generan los nombres de grupo para la tabla de precios de servicio.

class GrupoPrecios(models.Model):
	nombreDelGrupo	= models.CharField(max_length=50,unique = True)
	
	def __unicode__(self):
		DatosGrupo = "%s"%(self.nombreDelGrupo)
		return DatosGrupo

# Modelo de Grupo de Precios. 
# Aqui se generan los nombres de grupo, de servicio y precio para la tabla de GrupoServicio.

class GrupoServicio(models.Model):
	nombreDelGrupo	= models.ForeignKey(GrupoPrecios)
	nombreDelServicio = models.ForeignKey(PrecioServicio)
	precio = models.IntegerField(max_length=10)

	def __unicode__(self):
		DatosServicios = "%s"%(self.nombreDelGrupo,self.nombreDelServicio,self.precio)
		return DatosServicios