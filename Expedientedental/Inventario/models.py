from django.db import models
from altas.models import Medico,Paciente
from decimal import Decimal

# Create your models here.

class InventarioInsumos(models.Model):
	tipo_insumo=models.CharField(max_length=50)
	nombre_producto =models.CharField(max_length=100)
	cantidad    =models.IntegerField(max_length=6)
	precio_unidad=models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
	fecha_entrada= models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		datos="%s %s"%(self.codigoproveedor,self.descripcion)
		return datos

class TipoPaquete(models.Model):
	nombrePaquete=models.CharField(max_length=50)


class InsumospPaquete(models.Model):
	inventario_insumos=models.ForeignKey(InventarioInsumos)
	paquete=models.ForeignKey(TipoPaquete)
	cantidad=models.IntegerField(max_length=2)

class SalidadeMaterial(models.Model):
	insumos_Salida=models.ForeignKey(InventarioInsumos)
	paciente	= models.ForeignKey(Paciente)
	medico	= models.ForeignKey(Medico)
	fechaSalida= models.DateTimeField(blank=True, null=True)
	
	def __unicode__(self):
		codeSalida="%s %s"%(self.ordendeSalida)
		return codeSalida

class InsumosSalida(models.Model):
	inventario_insumos=models.ForeignKey(InventarioInsumos)
	paquete_usado=models.ForeignKey(SalidadeMaterial)
	cantidad=models.IntegerField(max_length=2)



		


		