from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from ActividadesClinicas.views import interrogatorio
from ActividadesClinicas.views import odontograma
<<<<<<< HEAD
from cotizacion.views import Cotizacion
=======
<<<<<<< HEAD
from ActividadesClinicas.views import diagnosticos

from Inventario.views import categoriaProducto
from Inventario.views import producto
from Inventario.views import tipoPaquete
from Inventario.views import paquete

=======
from cotizacion.views import cotizacion
>>>>>>> 9cdd696c122285da30b935301474ff2d43dc0070
#from ActividadesClinicas.views import interrogatorio
#from ActividadesClinicas.views import Odontograma
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
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
    

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^interrogatorio/$',interrogatorio),
    url(r'^odontograma/$',odontograma),
<<<<<<< HEAD
    url(r'^Cotizacion/$',Cotizacion),
=======
<<<<<<< HEAD
    url(r'^diagnosticos/$',diagnosticos),

    url(r'^categoriaProd/$',categoriaProducto),
    url(r'^paquete/$',paquete),
    url(r'^producto/$',producto),
    url(r'^tipoPaquete/$',tipoPaquete),
=======
    url(r'^cotizacion/$',cotizacion),
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
>>>>>>> 9cdd696c122285da30b935301474ff2d43dc0070
)
