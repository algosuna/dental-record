<<<<<<< HEAD
from django.conf.urls.defaults import *
from django.views.generic import ListView
from cotizaciones.models import Cotizacion

urlpatterns = patterns('',
	url(r'^create/$', 'cotizaciones.views.create'), #create
=======
from django.conf.urls.defaults import patterns,url
from django.views.generic import ListView
from cotizacion.models import Cotizacion

urlpatterns = patterns('',
	url(r'^create/$', 'cotizacion.views.create'), #create
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56
	url(r'^$',
        ListView.as_view(
            queryset = Cotizacion.objects.order_by('id'),
            context_object_name = 'latest_list', 
<<<<<<< HEAD
            template_name = 'cotizaciones/index.html')), #read
	url(r'^update/(?P<id_cotizacion>\d+)/$', 'cotizaciones.views.update'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/printit$', 'cotizaciones.views.update_printit'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/details/create$', 'cotizaciones.views.details_create'), #create
	url(r'^update/(?P<id_cotizacion>\d+)/details/update/(?P<id_cotizaciondetail>\d+)/$', 'cotizaciones.views.details_update'), #create
)
=======
            template_name = 'index.html')), #read
	url(r'^update/(?P<id_cotizacion>\d+)/$', 'cotizacion.views.update'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/printit$', 'cotizacion.views.update_printit'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/details/create$', 'cotizacion.views.details_create'), #create
	url(r'^update/(?P<id_cotizacion>\d+)/details/update/(?P<id_cotizaciondetail>\d+)/$', 'cotizacion.views.details_update'), #create
	url(r'^delete/(?P<id_cotizacion>\d+)/$', 'cotizacion.views.delete_update',),  #delete
)
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56
