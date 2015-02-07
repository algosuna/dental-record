from django.db import models

# Create your models here.

# Modelo de Precios de Servicios

class precioservicio(models.Model):
	Nombre_del_Servicio	= models.CharField(max_length=50)
	Precio = models.IntegerField(max_length=10)

	def __unicode__(self):
		Servicio = "%s"%(self.Nombre_del_Servicio)

		return Servicio
	def __unicode__(self):
		Precio = "%s"%(self.Precio)
		return Precio


# Modelo de Grupo de Precios. 
# Aqui se generan los nombres de grupo para la tabla de precios de servicio.

class grupoprecios(models.Model):
	Nombre_del_Grupo	= models.CharField(max_length=50)
	Precio = models.ForeignKey(precioservicio)

	def __unicode__(self):
		DatosGrupo = "%s %s"%(self.Nombre_del_Grupo,self.Precio)
		return DatosGrupo