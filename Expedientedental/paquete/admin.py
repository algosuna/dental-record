from django.contrib import admin
from paquete.models import Paquete
from paquete.models import EntryPaquete
from Inventario.views import *




class PaqueteAdmin(admin.ModelAdmin):
	class Meta:
			model=Paquete

class EntryPaqueteAdmin(admin.ModelAdmin):
	filter_horizontal=('producto',)



admin.site.register(EntryPaquete,EntryPaqueteAdmin)
admin.site.register(Paquete,PaqueteAdmin)
	