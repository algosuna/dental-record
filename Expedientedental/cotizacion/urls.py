from django.conf.urls.defaults import patterns, url
from cotizacion.views import CotizacionPDF

urlpatterns = patterns(
    'cotizacion.views',

    # main, the  flow starts here
    url(r'^$', 'pending_orders'),

    # review the items in cotizacion, select approved items
    url(r'^(?P<odontograma_id>\d+)/$', 'cotizacion', name='cotizacion'),

)
urlpatterns +=patterns(
    '',
    #reporte de cotizacion)
    url(r'^cotizacion/(?P<cotizacion_id>\d+)/pdf/$',
        CotizacionPDF.as_view()),
    )
