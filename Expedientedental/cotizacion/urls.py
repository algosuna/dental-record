from django.conf.urls.defaults import patterns, include, url

from cotizacion.models import Cotizacion

urlpatterns = patterns('cotizacion.views',

    # main, the  flow starts here
	url(r'^$', 'pending_orders'),

    url(r'^create/$', 'create'), #create
	url(r'^update/(?P<id_cotizacion>\d+)/$', 'update', name='cotizacion-detail'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/printit$', 'update_printit'), #update
	url(r'^update/(?P<id_cotizacion>\d+)/details/create/$', 'details_create', name='detail'), #create
	url(r'^update/(?P<id_cotizacion>\d+)/details/update/(?P<id_cotizaciondetail>\d+)/$', 'details_update'), #create

)
