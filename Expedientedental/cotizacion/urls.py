from django.conf.urls.defaults import patterns, url
from cotizacion.views import CotizacionPDF, CotizacionList, ProcesadoList

urlpatterns = patterns(
    'cotizacion.views',

    url(r'^$', CotizacionList.as_view(), name='cotizacion_list'),

    # review the items in cotizacion, select approved items
    url(r'^(?P<pk>\d+)/detail/$',
        'cotizacion_detail', name='cotizacion_detail'),

    url(r'^procesados/$', ProcesadoList.as_view(), name='procesado_list'),

    # reporte de cotizacion
    url(r'^(?P<pk>\d+)/pdf/$', CotizacionPDF.as_view(), name='pdf'),
)
