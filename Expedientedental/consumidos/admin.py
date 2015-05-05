from django.contrib import admin
from consumidos.models import Paquete, PaqueteItem, PaqueteConsumido, \
    PaqueteConsumidoItem


class PaqueteConsumidoAdmin(admin.ModelAdmin):
    list_display = [
        'paquete',
        'medico',
        'fecha',
    ]
    list_filter = [
        'medico',
        'fecha',
        'paquete',
    ]

admin.site.register(Paquete)
admin.site.register(PaqueteItem)
admin.site.register(PaqueteConsumido)  # ,PaqueteConsumidoAdmin)
admin.site.register(PaqueteConsumidoItem)
