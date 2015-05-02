from django.contrib import admin

from servicios.models import PaqueteServicios, Servicio


class PaqueteAdmin(admin.ModelAdmin):
    pass


class ServicioAdmin(admin.ModelAdmin):
    pass


admin.site.register(PaqueteServicios, PaqueteAdmin)
admin.site.register(Servicio, ServicioAdmin)
