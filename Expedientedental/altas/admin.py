from django.contrib	import *
from altas.models import *

class medicoAdmin(admin.ModelAdmin):
	list_display = ('Nombre')
	list_filter = ('Nombre')
	search_fields = ['Nombre']
	fields = ('Nombre')

class pacienteAdmin(admin.ModelAdmin):
	list_display = ('Nombre')
	list_filter = ('Nombre')
	search_fields = ['Nombre']
	fields = ('Nombre')

admin.site.register(medico)
admin.site.register(paciente)