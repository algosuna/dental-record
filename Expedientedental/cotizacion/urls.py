from django.conf.urls.defaults import patterns, include, url

from cotizacion.models import Cotizacion

urlpatterns = patterns('cotizacion.views',

    # main, the  flow starts here
	url(r'^$', 'pending_orders'),

    # review the items in cotizacion, select approved items
    url(r'^(?P<odontograma_id>\d+)/$', 'cotizacion', name='cotizacion'),

)
