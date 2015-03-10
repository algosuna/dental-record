from django.db import models
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from cotizacion.models import CotizacionDetail,Cotizacion



# Create your models here.



class DateTime(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.fecha.strftime("%b %d, %Y, %I:%M %p"))

class HistogramaItem(models.Model):
    folio        = models.ForeignKey(Cotizacion)
    servicio     = models.ManyToManyField(CotizacionDetail)
    inicio       = models.DateTimeField(auto_now_add=True)  
    estimado     = models.DateTimeField(auto_now_add=True)
    finalizado   = models.DateTimeField(auto_now_add=True)
    

    def __unicode__(self):
        return "%s"%(self.folio)
    #onhold = models.BooleanField(default=False)
   
    

    

