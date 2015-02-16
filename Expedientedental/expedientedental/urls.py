from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ActividadesClinicas.views import interrogatorio
from ActividadesClinicas.views import odontograma
from ActividadesClinicas.views import diagnosticos
from ActividadesClinicas.views import datospaciente
from Inventario.views import Producto
from cotizacion.views import Cotizacion

<<<<<<< HEAD
#from ActividadesClinicas.views import interrogatorio
#from ActividadesClinicas.views import Odontograma 
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
#from ActividadesClinicas.views import interrogatorio
#from ActividadesClinicas.views import Odontograma
=======

>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
>>>>>>> f8d12bebf2b6c2fd2b1f0dccb68bc39f3f32d999
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56
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
<<<<<<< HEAD
    #url(r'^',include('cotizacion.urls')),
    url(r'^cotizacion/', include('cotizacion.urls')),
=======
<<<<<<< HEAD
=======

>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
>>>>>>> f8d12bebf2b6c2fd2b1f0dccb68bc39f3f32d999
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^interrogatorio/$',interrogatorio),
    url(r'^odontograma/$',odontograma),
    url(r'^diagnosticos/$',diagnosticos),
<<<<<<< HEAD
    url(r'^detail/$',Cotizacion),
    #url(r'^categoriaProd/$',categoriaProducto),
    #url(r'^paquete/$',Paquete),
    url(r'^producto/$',Producto),
        

    #url(r'^tipoPaquete/$',tipoPaquete),

   
    #url(r'^prueba/$',busqueda),
=======
    url(r'^categoriaProd/$',categoriaProducto),
    url(r'^paquete/$',paquete),
    url(r'^producto/$',producto),
    url(r'^tipoPaquete/$',tipoPaquete),
<<<<<<< HEAD
=======
    url(r'^cotizacion/$',Cotizacion),
<<<<<<< HEAD
=======
    #url(r'^prueba/$',busqueda),
>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
>>>>>>> f8d12bebf2b6c2fd2b1f0dccb68bc39f3f32d999
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56
)
