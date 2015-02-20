from django.contrib	import admin
from ActividadesClinicas.models import HistoriaClinica
from ActividadesClinicas.models import ListadeDiagnosticos
from ActividadesClinicas.models import Odontograma

class HistoriaClinicaAdmin(admin.ModelAdmin):
	list_display = ('medico','paciente',)
	list_filter = ('medico','paciente',)
	search_fields = ['medico','paciente']
	fields = ()

class ListadeDiagnosticosAdmin(admin.ModelAdmin):
	list_display = ('codigoDiagnostico','nombreDiagnostico',)
	list_filter = ('codigoDiagnostico','nombreDiagnostico',)
	search_fields = ['codigoDiagnostico','nombreDiagnostico']
	fields = ()

class OdontogramaAdmin(admin.ModelAdmin):
	list_display = ('doctor','paciente','problemaDental',)
	list_filter = ('doctor','paciente','problemaDental',)
	search_fields = ['doctor','paciente','problemaDental']
	fields = ()

admin.site.register(HistoriaClinica,HistoriaClinicaAdmin)
admin.site.register(ListadeDiagnosticos,ListadeDiagnosticosAdmin)
admin.site.register(Odontograma,OdontogramaAdmin)
