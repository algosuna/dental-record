from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Inventario.views import producto, categoria
from cotizacion.views import Cotizacion
from paquete.views import paquete, tipoPaquete
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dental.views.home', name='home'),
    # url(r'^dental/', include('dental.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^',include('altas.urls')),
    url(r'^',include('precios.urls')),
    url(r'^',include('bitacora.urls')),
    #url(r'^',include('cotizacion.urls')),
    url(r'^cotizacion/', include('cotizacion.urls')),
    url(r'^', include('ActividadesClinicas.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^producto/$',producto),
    url(r'^categoria/$',categoria),

    url(r'^paquete/$',paquete),
    url(r'^tipoPaquete/$',tipoPaquete),
    url(r'^evaluacion/$', 'buscarpaciente'),
    url(r'^detalles/$', 'detallespaciente'),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

    #url(r'^prueba/$',busqueda),

)


