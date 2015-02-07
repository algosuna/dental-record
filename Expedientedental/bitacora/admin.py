from django.contrib	import admin
from bitacora.models import bitacora
from bitacora.models import notas

'''
class notasAdmin(admin.ModelAdmin):
	list_display = ('id','Descripcion','Fecha_y_Hora')
	list_filter = ('Descripcion','Fecha_y_Hora')
	search_fields = ['Descripcion','Fecha_y_Hora']
	fields = ('Descripcion','Fecha_y_Hora')

class bitacoraAdmin(admin.ModelAdmin):
	list_display = ('Nombre_del_Procedimiento','Fecha_y_Hora','numero_de_nota')
	list_filter = ('Nombre_del_Procedimiento','Fecha_y_Hora','numero_de_nota')
	search_fields = ['Nombre_del_Procedimiento','Fecha_y_Hora','numero_de_nota']
	fields = ('Nombre_del_Procedimiento','Fecha_y_Hora','numero_de_nota')
<<<<<<< HEAD

admin.site.register(notas,notasAdmin)
admin.site.register(bitacora,bitacoraAdmin)
'''
=======
'''
admin.site.register(notas)
admin.site.register(bitacora)
>>>>>>> eb6ad5b6e2f16f8d923d4958e25b7f5ad0bd7a2f
