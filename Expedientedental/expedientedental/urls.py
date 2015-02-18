from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from ActividadesClinicas.views import interrogatorio
from ActividadesClinicas.views import odontograma
from ActividadesClinicas.views import diagnosticos
from ActividadesClinicas.views import datospaciente
from Inventario.views import Producto
<<<<<<< HEAD
from django.contrib import admin

=======
from cotizacion.views import Cotizacion



>>>>>>> 9debe0c436b85be322a302cd9c0553720d79d3e4
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

    #url(r'^',include('cotizacion.urls')),
>>>>>>> 9debe0c436b85be322a302cd9c0553720d79d3e4
    url(r'^cotizacion/', include('cotizacion.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^interrogatorio/$',interrogatorio),
    url(r'^odontograma/$',odontograma),
    url(r'^diagnosticos/$',diagnosticos),
<<<<<<< HEAD
    url(r'^producto/$',Producto),
    #url(r'^prueba/$',busqueda),

)
=======
    

   # url(r'^detail/$',Cotizacion),
    #url(r'^categoriaProd/$',categoriaProducto),
    #url(r'^paquete/$',Paquete),
    #url(r'^producto/$',Producto),
        

    #url(r'^tipoPaquete/$',tipoPaquete),

   
    #url(r'^prueba/$',busqueda),

    #url(r'^categoriaProd/$',categoriaProducto),
   # url(r'^paquete/$',paquete),
    #url(r'^producto/$',producto),
    #url(r'^tipoPaquete/$',tipoPaquete),
    )

>>>>>>> 9debe0c436b85be322a302cd9c0553720d79d3e4
