from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from Inventario.views import productoView, unidadView, busqueda, detallesProd,\
    ingresarCantidad, EditProductView
from procesocoopago.views import Pago, Proceso

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

urlpatterns = patterns(
    '',

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^altas/', include('altas.urls')),
    url(r'^clinica/', include('clinica.urls')),
    url(r'^cotizacion/', include('cotizacion.urls')),

    url(r'^', include('paquete.urls')),
    url(r'^', include('precios.urls')),

    url(r'^producto/$', productoView),

    url(r'^producto/unidad/$', unidadView),
    url(r'^producto/edit/(?P<pk>\d+)$', EditProductView.as_view(),
        name='producto-edit'),


    url(r'^ingresar/(?P<entrada_id>\d+)$', ingresarCantidad),
    url(r'^detalles_producto/(?P<entrada_id>\d+)$', detallesProd),
    url(r'^entradas/$', busqueda),

    url(r'^pago/$', Pago),
    url(r'^proceso/$', Proceso),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    (r'^dajaxice/', include('dajaxice.urls')),
)
