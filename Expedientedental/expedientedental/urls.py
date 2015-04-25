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

    # url(r'^', include('django.contrib.auth.urls')),

    url(r'^', include('accounts.urls')),

    url(r'^altas/', include('altas.urls')),
    url(r'^clinica/', include('clinica.urls')),
    url(r'^cotizacion/', include('cotizacion.urls')),
    url(r'^pagos/', include('pagos.urls')),
    url(r'^inventario/', include('Inventario.urls')),

    url(r'^', include('servicios.urls')),
    url(r'^', include('paquete.urls')),
    url(r'^', include('precios.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    (r'^dajaxice/', include('dajaxice.urls')),
)
