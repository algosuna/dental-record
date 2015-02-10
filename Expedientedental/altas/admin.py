from django.contrib	import admin
from altas.models import Medico
from altas.models import Paciente

class medicoAdmin(admin.ModelAdmin):
	list_display = ('medico','apellidoPaterno',)
	list_filter = ('medico','apellidoPaterno',)
	search_fields = ['medico','apellidoPaterno']
	fields = ()


class pacienteAdmin(admin.ModelAdmin):
	list_display = ('paciente','apellidoPaterno',)
	list_filter = ('paciente','apellidoPaterno',)
	search_fields = ['paciente','apellidoPaterno']
	fields = ()

admin.site.register(Medico,medicoAdmin)
admin.site.register(Paciente,pacienteAdmin)
