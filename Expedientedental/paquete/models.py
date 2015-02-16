# -*- encoding: utf-8 -*-
from django.db import models
from Inventario.models import Producto
from Inventario.views import *


class Paquete(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)

	def __unicode__(self):
		return'%s' %(self.nombre)





class EntryPaquete(models.Model):
	nombre=models.ForeignKey(Paquete)
	producto= models.ManyToManyField(Producto)
	cantidad=models.IntegerField()

	def __unicode__(self):
		return '%s' % (self.producto)

	def __str__(self):
		return '%s' % (self.producto)	
	

# Create your models here.
