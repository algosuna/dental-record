from django.contrib	import admin
from ActividadesClinicas.models import Interrogatorio
from ActividadesClinicas.models import ListadeDiagnosticos
from ActividadesClinicas.models import Odontograma
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

admin.site.register(Interrogatorio)
admin.site.register(ListadeDiagnosticos)
admin.site.register(Odontograma)
