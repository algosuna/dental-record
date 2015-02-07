from django.contrib	import *
from altas.models import medico

class medicoAdmin(admin.ModelAdmin):
	list_display = ('nombre')
	list_filter = ('nombre')
	search_fields = ['nombre']
	fields = ('nombre')

'''
class pacienteAdmin(admin.ModelAdmin):
	list_display = ('nombre')
	list_filter = ('nombre')
	search_fields = ['nombre']
	fields = ('nombre')
'''

admin.site.register(medico)
#admin.site.register(paciente)