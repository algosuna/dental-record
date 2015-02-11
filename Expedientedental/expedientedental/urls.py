from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from ActividadesClinicas.views import interrogatorio
from ActividadesClinicas.views import odontograma
<<<<<<< HEAD
=======
<<<<<<< HEAD
from cotizacion.views import Cotizacion
=======
<<<<<<< HEAD
>>>>>>> 2557d746b39d5b4988c01575dcbe06f2d30b2d72
from ActividadesClinicas.views import diagnosticos
from ActividadesClinicas.views import datospaciente

from Inventario.views import categoriaProducto
from Inventario.views import producto
from Inventario.views import tipoPaquete
from Inventario.views import paquete
from cotizacion.views import cotizacion
<<<<<<< HEAD

=======
>>>>>>> 9cdd696c122285da30b935301474ff2d43dc0070
#from ActividadesClinicas.views import interrogatorio
#from ActividadesClinicas.views import Odontograma
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
>>>>>>> 2557d746b39d5b4988c01575dcbe06f2d30b2d72
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
    #url(r'^odontograma/$',odontograma),
    url(r'^odontograma/$',odontograma),
<<<<<<< HEAD
=======
<<<<<<< HEAD
    url(r'^Cotizacion/$',Cotizacion),
=======
<<<<<<< HEAD
>>>>>>> 2557d746b39d5b4988c01575dcbe06f2d30b2d72
    url(r'^diagnosticos/$',diagnosticos),
    url(r'^categoriaProd/$',categoriaProducto),
    url(r'^paquete/$',paquete),
    url(r'^producto/$',producto),
    url(r'^tipoPaquete/$',tipoPaquete),
    url(r'^cotizacion/$',cotizacion),
<<<<<<< HEAD
=======
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
>>>>>>> 9cdd696c122285da30b935301474ff2d43dc0070
>>>>>>> 2557d746b39d5b4988c01575dcbe06f2d30b2d72
)
