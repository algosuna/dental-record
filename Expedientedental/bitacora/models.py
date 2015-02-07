from django.db import models

# Create your models here.

# Modelo de Notas Agregadas

class notas(models.Model):
	Descripcion	= models.TextField()
	Fecha_y_Hora = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		Nota = "%s %s"%(self.Descripcion,self.Fecha_y_Hora)
		return Nota


# Modelo de Bitacora de Procedimientos

class bitacora(models.Model):
	Nombre_del_Procedimiento = models.CharField(max_length=70)
	Fecha_y_Hora = models.DateTimeField(blank=True, null=True)
	numero_de_nota = models.ForeignKey(notas)

	def __unicode__(self):
		DatosBitacora = "%s %s"%(self.numero_de_nota,self.Nombre_del_Procedimiento,self.Fecha_y_Hora)
		return DatosBitacora