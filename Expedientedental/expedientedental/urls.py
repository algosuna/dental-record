import settings

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from ActividadesClinicas.views import HistoriaClinica, odontograma, diagnosticos, datospaciente, buscarpaciente
from Inventario.views import producto, categoria
from paquete.views import paquete, tipoPaquete
from procesocoopago.views import Abono, Pago, Proceso

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dental.views.home', name='home'),
    # url(r'^dental/', include('dental.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('ActividadesClinicas.urls')),

    url(r'^', include('paquete.urls')),
    url(r'^',include('altas.urls')),
    url(r'^',include('precios.urls')),
    url(r'^',include('bitacora.urls')),

    url(r'^cotizacion/', include('cotizacion.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^producto/$',producto),
    url(r'^categoria/$',categoria),


    url(r'^paquete/$',paquete),
    url(r'^tipoPaquete/$',tipoPaquete),
    url(r'^abono/$',Abono),
    url(r'^pago/$',Pago),
    url(r'^proceso/$',Proceso),


    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

    #url(r'^prueba/$',busqueda),
    
    (r'^dajaxice/', include('dajaxice.urls')),
)


