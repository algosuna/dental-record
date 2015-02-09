from django.db import models
from altas.models import Medico,Paciente
from decimal import Decimal

# Create your models here.
# Realizar views cuando termine Ray
'''
class InventarioInsumos(models.Model):
	codigoProveedor=models.CharField(max_length=70)
	descripcion =models.CharField(max_length=100)
	cantidad    =models.IntegerField(max_length=6)
	precioUnidad=models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
	fechaEntrada= models.DateTimeField(blank=True, null=True)
	precioCaja = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)

	def __unicode__(self):
		datos="%s %s"%(self.codigoproveedor,self.descripcion)
		return datos


	
	

class Paquetes(models.Model):
	nombrePaquete=models.CharField(max_length=50)
	codigoProveedor=models.ForeignKey(InventarioInsumos, null =True , related_name='codigoprovee')
	descripcion = models.ForeignKey(InventarioInsumos, null=True, related_name='descripcion')
	precioUnidad=codigoproveedor=models.ForeignKey(InventarioInsumos, null =True , related_name='precioUnidad')
	unidades=models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)

	def __unicode__(self):
		nombrePaq="%s %s"%(self.nombrePaquete)
		return nombrePaq

		
class SalidadeMaterial(models.Model):
	ordendeSalida=models.IntegerField(unique=True ,max_length=8)
	paciente	= models.ForeignKey(Paciente)
	medico	= models.ForeignKey(Medico)
	fechaSalida= models.DateTimeField(blank=True, null=True)
	
	def __unicode__(self):
		codeSalida="%s %s"%(self.ordendeSalida)
		return codeSalida
'''
		