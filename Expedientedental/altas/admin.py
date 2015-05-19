from django.contrib import admin

from altas.models import Medico, Paciente, Grupo


class PacienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Grupo)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico)
