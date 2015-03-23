from django.contrib	import admin
from altas.models import Medico, Paciente,Grupo

class medicoAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidoPaterno',)
	list_filter = ('nombre','apellidoPaterno',)
	search_fields = ['nombre','apellidoPaterno']
	fields = ()


class pacienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','apellidoPaterno',)
	list_filter = ('id','nombre','apellidoPaterno',)
	search_fields = ['id','nombre','apellidoPaterno']
	fields = ()

admin.site.register(Medico,medicoAdmin)
admin.site.register(Grupo)
admin.site.register(Paciente,pacienteAdmin)
