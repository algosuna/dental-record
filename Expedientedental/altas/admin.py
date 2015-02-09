from django.contrib	import admin
from altas.models import Medico
from altas.models import Paciente

class medicoAdmin(admin.ModelAdmin):
	list_display = ('nombre')
	list_filter = ('nombre')
	search_fields = ['nombre']
	fields = ('nombre')


class pacienteAdmin(admin.ModelAdmin):
	list_display = ('nombre')
	list_filter = ('nombre')
	search_fields = ['nombre']
	fields = ('nombre')

admin.site.register(Medico)
admin.site.register(Paciente)
