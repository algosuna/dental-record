from django.contrib	import *
from precios.models import *
'''
class precioservicioAdmin(admin.ModelAdmin):
	list_display = ('Nombre_del_Servicio','Precio')
	list_filter = ('Nombre_del_Servicio','Precio')
	search_fields = ['Nombre_del_Servicio','Precio']
	fields = ('Nombre_del_Servicio','Precio')

class grupopreciosAdmin(admin.ModelAdmin):
	list_display = ('Nombre_del_Grupo','Precio')
	list_filter = ('Nombre_del_Grupo','Precio')
	search_fields = ['Nombre_del_Grupo','Precio']
	fields = ('Nombre_del_Grupo','Precio')

admin.site.register(precioservicio,precioservicioAdmin)
admin.site.register(grupoprecios,grupopreciosAdmin)
'''