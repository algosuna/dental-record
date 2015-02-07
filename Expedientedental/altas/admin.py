<<<<<<< HEAD
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
=======
from django.contrib	import admin
from altas.models import Medico
from altas.models import Paciente

#class MedicoAdmin(admin.ModelAdmin):
#	list_display = ('Nombre')
#	list_filter = ('Nombre')
#	search_fields = ['Nombre']
#	fields = ('Nombre')

#class PacienteAdmin(admin.ModelAdmin):
#	list_display = ('Nombre')
#	list_filter = ('Nombre')
#	search_fields = ['Nombre']
#	fields = ('Nombre')

admin.site.register(Medico)
admin.site.register(Paciente)
>>>>>>> eb6ad5b6e2f16f8d923d4958e25b7f5ad0bd7a2f
