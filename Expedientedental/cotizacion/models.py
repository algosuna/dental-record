from django.db import models

from core.models import TimeStampedModel
from ActividadesClinicas.models import Procedimiento, Odontograma
from precios.models import PrecioTratamiento


class Cotizacion(TimeStampedModel):
	odontograma = models.ForeignKey(Odontograma, null=True)


class CotizacionItemManager(models.Manager):
	def create_items(self, cotizacion):
		odontograma = cotizacion.odontograma

		procedimiento_qs = odontograma.procedimiento_set.all()
		grupo = odontograma.paciente.grupo
		items = []
		for procedimiento in procedimiento_qs:

			precio = PrecioTratamiento.objects.get(
				grupo = grupo,
				tratamiento = procedimiento.tratamiento
			).precio
			item = self.create(
				status = 'pendiente',
				cotizacion = cotizacion,
				precio = precio,
				procedimiento = procedimiento
			)
			items.append(item)

		return items


class CotizacionItem(TimeStampedModel):
	STATUS_CHOICES=(
		('aceptado','Aceptado'),
		('pendiente','Pendiente'),
	)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aceptado')
	cotizacion = models.ForeignKey(Cotizacion)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	procedimiento = models.ForeignKey(Procedimiento)

	objects = CotizacionItemManager()

	def __unicode__(self):
		return "(%s) %s"%(self.cotizacion,self.procedimiento)

