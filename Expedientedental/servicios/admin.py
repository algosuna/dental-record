from django.contrib import admin

from servicios.models import Paquete, Servicio


class PaqueteAdmin(admin.ModelAdmin):
    pass


class ServicioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(Servicio, ServicioAdmin)
