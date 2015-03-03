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




class HistogramaItemAdmin(admin.ModelAdmin):
    list_display = ["nombre", "prioridad", "dificultad", "inicio", "progreso_",
                    "delete", "onhold", "hecho"]
    list_filter = ["prioridad", "dificultad", "onhold", "hecho"]
    search_fields = ["nombre"]


class ItemInline(admin.TabularInline):
    model = HistogramaItem


class DateAdmin(admin.ModelAdmin):
    list_display = ["fecha"]
    inlines = [ItemInline]
    

   

admin.site.register(HistogramaItem, HistogramaItemAdmin)
admin.site.register(DateTime, DateAdmin)