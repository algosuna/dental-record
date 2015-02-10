from django.db import models
from altas.models import Medico,Paciente
from decimal import Decimal

# Create your models here.
<<<<<<< HEAD

# Realizar views cuando termine Ray

class InventarioInsumos(models.Model):
	codigoProveedor=models.CharField(max_length=70)
	descripcion =models.CharField(max_length=100)
	cantidad    =models.IntegerField(max_length=6)
	precioUnidad=models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
	fechaEntrada= models.DateTimeField(blank=True, null=True)
	precioCaja = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
=======
>>>>>>> 17bfec642523457885df05d846a6b8d4d2340040

# Realizar views cuando termine Ray
class categoriaProducto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=400)
	def __unicode__(self):
		return self.nombre

<<<<<<< HEAD
=======

>>>>>>> 17bfec642523457885df05d846a6b8d4d2340040
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


<<<<<<< HEAD
=======

>>>>>>> 17bfec642523457885df05d846a6b8d4d2340040
class paquete(models.Model):
	nombre      = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	status      = models.BooleanField(default=True)
	precio      = models.DecimalField(max_digits=6,decimal_places=2)
	stock       = models.IntegerField()
	categorias  = models.ManyToManyField(tipoPaquete,null=True,blank=True)
	def __unicode__(self):
<<<<<<< HEAD

		codeSalida="%s %s"%(self.ordendeSalida)
		return codeSalida
		return self.nombre
    	#retornar nombre del paquete para presentar una descripcion en el panel

		
=======
		return self.nombre

    	#retornar nombre del paquete para presentar una descripcion en el panel


>>>>>>> 17bfec642523457885df05d846a6b8d4d2340040
