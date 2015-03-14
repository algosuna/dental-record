from django.db import models

from cotizacion.models import CotizacionItem, Cotizacion


class DateTime(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.fecha.strftime("%b %d, %Y, %I:%M %p"))


class HistogramaItem(models.Model):
    folio = models.ForeignKey(Cotizacion)
    servicio = models.ManyToManyField(CotizacionItem)
    inicio = models.DateTimeField(auto_now_add=True)
    estimado = models.DateTimeField(auto_now_add=True)
    finalizado = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s"%(self.folio)
