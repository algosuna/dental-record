from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin

from dajaxice.core import dajaxice_autodiscover

admin.autodiscover()

dajaxice_autodiscover()

urlpatterns = patterns(
    '',

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^altas/', include('altas.urls', namespace='altas')),
    url(r'^clinica/', include('clinica.urls', namespace='clinica')),
    url(r'^presupuesto/', include('cotizacion.urls', namespace='cotizacion')),
    url(r'^pagos/', include('pagos.urls', namespace='pagos')),
    url(r'^utilidad/', include('utilidad.urls', namespace='calculos')),
    url(r'^inventario/', include('inventario.urls', namespace='inventario')),

    url(r'^', include('servicios.urls', namespace='servicios')),
    url(r'^', include('precios.urls', namespace='precios')),
    url(r'^', include('consumidos.urls', namespace='consumidos')),

    # Esto es necesario para tener un folder de media funcional.
    # Agregado para foto de paciente (imagenpaciente)
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^dajaxice/', include('dajaxice.urls')),
)
