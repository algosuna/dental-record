from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from altas.models import Medico, Paciente, Grupo


# class medicoAdmin(admin.ModelAdmin):
#     pass


class PacienteAdmin(admin.ModelAdmin):
    pass


# Define an inline admin descriptor for Medico model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = Medico
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Medico, medicoAdmin)
admin.site.register(Grupo)
admin.site.register(Paciente, PacienteAdmin)
