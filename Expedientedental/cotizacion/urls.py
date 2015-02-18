from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from cotizacion.models import Cotizacion

urlpatterns = patterns('',
	url(r'^create/$', 'cotizacion.views.create'), #create
	url(r'^$',
        ListView.as_view(
            queryset = Cotizacion.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = '/index.html')), #read
	url(r'^update/(?P<id_cotizacion>\d+)/$', 'cotizacion.views.update'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/printit$', 'cotizacion.views.update_printit'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/details/create/$', 'cotizacion.views.details_create'), #create
	url(r'^update/(?P<id_cotizacion>\d+)/details/update/(?P<id_cotizaciondetail>\d+)/$', 'cotizacion.views.details_update'), #create

)

