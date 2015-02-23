from django.db import models
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your models here.



class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.datetime.strftime("%b %d, %Y, %I:%M %p"))

class histogramaItem(models.Model):
    name = models.CharField(max_length=60)
    created = models.ForeignKey(DateTime)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    #onhold = models.BooleanField(default=False)
   
    

    def progress_(self):
        return """
        <div id="progress_cont_%s" class="progress_cont">
        <div id="progress_btns_%s" class="progress_btns">
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
         <div id="progress_on_%s" class="progress_on">&nbsp;</div>
         <div id="progress_%s" style="visibility: hidden"></div>
         </div>
            """ % (self.pk, self.pk, self.pk, self.pk)

    progress_.allow_tags = True
    progress_.admin_order_field = "progress"
