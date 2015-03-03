from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ActividadesClinicas.views import HistoriaClinica
from ActividadesClinicas.views import odontograma
from ActividadesClinicas.views import diagnosticos
from ActividadesClinicas.views import datospaciente
from ActividadesClinicas.views import detallespaciente
from ActividadesClinicas.views import buscarpaciente
from Inventario.views import producto, categoria
from cotizacion.views import Cotizacion
from paquete.views import paquete, tipoPaquete
from django.contrib import admin
from procesocoopago.views import Abono
from procesocoopago.views import Pago
from procesocoopago.views import Proceso

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

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^interrogatorio/$',HistoriaClinica),
    url(r'^odontograma/$',odontograma),
    url(r'^diagnosticos/$',diagnosticos),

    url(r'^producto/$',producto),
    url(r'^categoria/$',categoria),

    url(r'^paquete/$',paquete),
    url(r'^tipoPaquete/$',tipoPaquete),
    url(r'^evaluacion/$',buscarpaciente),
    url(r'^detalles/$',detallespaciente),
    url(r'^abono/$',Abono),
    url(r'^pago/$',Pago),
    url(r'^proceso/$',Proceso),


    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

    #url(r'^prueba/$',busqueda),
    
    (r'^dajaxice/', include('dajaxice.urls')),
)


