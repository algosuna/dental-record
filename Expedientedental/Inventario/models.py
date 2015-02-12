from django.db import models
from altas.models import Medico,Paciente
from decimal import Decimal

# Create your models here.

<<<<<<< HEAD
# Realizar views cuando termine Ray
=======
>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
class categoriaProducto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=400)
	def __unicode__(self):
		return self.nombre


class producto(models.Model):
	nombre      = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	status      = models.BooleanField(default=True)
	precio      = models.DecimalField(max_digits=6,decimal_places=2)
	stock       = models.IntegerField()
	categorias  = models.ManyToManyField(categoriaProducto,null=True,blank=True)
	def __unicode__(self):
		return self.nombre

    	#retornar nombre del producto para presentar una descripcion en el panel

class tipoPaquete(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.TextField(max_length=400)
	def __unicode__(self):
		return self.nombre


class paquete(models.Model):
	nombre      = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	status      = models.BooleanField(default=True)
	precio      = models.DecimalField(max_digits=6,decimal_places=2)
	stock       = models.IntegerField()
	categorias  = models.ManyToManyField(tipoPaquete,null=True,blank=True)
	def __unicode__(self):
<<<<<<< HEAD
		return self.nombre

    	#retornar nombre del paquete para presentar una descripcion en el panel

		codeSalida="%s %s"%(self.ordendeSalida)
		return codeSalida
		return self.nombre
    	#retornar nombre del paquete para presentar una descripcion en el panel

=======
		codeSalida="%s %s"%(self.nombre)
		return codeSalida

		#retornar nombre del paquete para presentar una descripcion en el panel
>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
