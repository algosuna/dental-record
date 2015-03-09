from django.db import models
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from cotizacion.models import CotizacionDetail



# Create your models here.



class DateTime(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.fecha.strftime("%b %d, %Y, %I:%M %p"))

class HistogramaItem(models.Model):
    
    servicio =models.ManyToManyField(CotizacionDetail)
    inicio = models.ForeignKey(DateTime)  
    hecho = models.BooleanField(default=False)
    onhold = models.BooleanField(default=False)
    progreso = models.IntegerField(default=0)

    def __unicode__(self):
        return "item %s"%(self.id)
    #onhold = models.BooleanField(default=False)
   
    

    def progreso_(self):
        return """
        <div id="progreso_cont_%s" class="progreso_cont">
        <div id="progreso_btns_%s" class="progreso_btns">
         <ul>
         <li>10</li>
         <li>20</li>
         <li>30</li>
         <li>40</li>
         <li>50</li>
         <li>60</li>
         <li>70</li>
         <li>80</li>
         <li>90</li>
         <li>100</li>
         </ul>
         </div>
         <div id="progreso_on_%s" class="progreso_on">&nbsp;</div>
         <div id="progreso_%s" style="visibility: hidden"></div>
         </div>
            """ % (self.pk, self.pk, self.pk, self.pk)

    progreso_.allow_tags = True
    progreso_.admin_order_field = "progreso"
