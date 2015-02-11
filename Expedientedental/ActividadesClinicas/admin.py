from django.contrib	import admin
from ActividadesClinicas.models import Interrogatorio
from ActividadesClinicas.models import ListadeDiagnosticos
from ActividadesClinicas.models import Odontograma

class InterrogatorioAdmin(admin.ModelAdmin):
	list_display = ('medico','paciente','observaciones','resumenClinico',)
	list_filter = ('medico','paciente','observaciones','resumenClinico',)
	search_fields = ['medico','paciente','observaciones','resumenClinico']
	fields = ()

class ListadeDiagnosticosAdmin(admin.ModelAdmin):
	list_display = ('codigoDiagnostico','nombreDiagnostico',)
	list_filter = ('codigoDiagnostico','nombreDiagnostico',)
	search_fields = ['codigoDiagnostico','nombreDiagnostico']
	fields = ()

class OdontogramaAdmin(admin.ModelAdmin):
	list_display = ('problemaDental',)
	list_filter = ('problemaDental',)
	search_fields = ['problemaDental']
	fields = ()

admin.site.register(Interrogatorio,InterrogatorioAdmin)
admin.site.register(ListadeDiagnosticos,ListadeDiagnosticosAdmin)
admin.site.register(Odontograma,OdontogramaAdmin)
