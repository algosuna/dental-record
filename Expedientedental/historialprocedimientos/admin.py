from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from historialprocedimientos.models import HistogramaItem,DateTime
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


class DateTimeAdmin(admin.ModelAdmin):
    list_display = ["fecha"]

class HistogramaItemAdmin(admin.ModelAdmin):
	class Meta:
		model=HistogramaItem
		exclude=('cotizacion',)
     
   

admin.site.register(HistogramaItem,HistogramaItemAdmin)
admin.site.register(DateTime,DateTimeAdmin)