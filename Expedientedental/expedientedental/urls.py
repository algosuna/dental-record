from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ActividadesClinicas.views import interrogatorio
from ActividadesClinicas.views import odontograma
from cotizacion.views import Cotizacion
from ActividadesClinicas.views import diagnosticos
<<<<<<< HEAD
=======
from ActividadesClinicas.views import datospaciente

>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
from Inventario.views import categoriaProducto
from Inventario.views import producto
from Inventario.views import tipoPaquete
from Inventario.views import paquete
from cotizacion.views import Cotizacion

<<<<<<< HEAD
#from ActividadesClinicas.views import interrogatorio
#from ActividadesClinicas.views import Odontograma
=======

>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
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
<<<<<<< HEAD
=======

>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^interrogatorio/$',interrogatorio),
    url(r'^odontograma/$',odontograma),
    url(r'^Cotizacion/$',Cotizacion),
    url(r'^diagnosticos/$',diagnosticos),
    url(r'^categoriaProd/$',categoriaProducto),
    url(r'^paquete/$',paquete),
    url(r'^producto/$',producto),
    url(r'^tipoPaquete/$',tipoPaquete),
    url(r'^cotizacion/$',Cotizacion),
<<<<<<< HEAD
=======
    #url(r'^prueba/$',busqueda),
>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
)
