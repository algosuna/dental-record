from django.conf.urls.defaults import *
from django.views.generic import ListView
from cotizaciones.models import Cotizacion

urlpatterns = patterns('',
	url(r'^create/$', 'cotizaciones.views.create'), #create
	url(r'^$',
        ListView.as_view(
            queryset = Cotizacion.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'cotizaciones/index.html')), #read
	url(r'^update/(?P<id_cotizacion>\d+)/$', 'cotizaciones.views.update'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/printit$', 'cotizaciones.views.update_printit'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/details/create$', 'cotizaciones.views.details_create'), #create
	url(r'^update/(?P<id_cotizacion>\d+)/details/update/(?P<id_cotizaciondetail>\d+)/$', 'cotizaciones.views.details_update'), #create
)