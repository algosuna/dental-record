from django.contrib	import admin
from altas.models import Medico, Paciente

class medicoAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidoPaterno',)
	list_filter = ('nombre','apellidoPaterno',)
	search_fields = ['nombre','apellidoPaterno']
	fields = ()


class pacienteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidoPaterno',)
	list_filter = ('nombre','apellidoPaterno',)
	search_fields = ['nombre','apellidoPaterno']
	fields = ()

admin.site.register(Medico,medicoAdmin)
admin.site.register(Paciente,pacienteAdmin)
