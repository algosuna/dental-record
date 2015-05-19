from django.contrib import admin

from altas.models import Medico, Paciente, Grupo

admin.site.register(Grupo)
admin.site.register(Paciente)
admin.site.register(Medico)
