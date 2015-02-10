from django.db import models
from altas.models import Medico,Paciente
from decimal import Decimal

# Create your models here.
<<<<<<< HEAD
=======





>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa

# Realizar views cuando termine Ray
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

=======

		codeSalida="%s %s"%(self.ordendeSalida)
		return codeSalida
		return self.nombre
    	#retornar nombre del paquete para presentar una descripcion en el panel
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
