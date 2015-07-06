from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.CotizacionList.as_view(), name='cotizacion_list'),

    # review the items in cotizacion, select approved items
    url(r'^(?P<pk>\d+)/detail/$',
        views.cotizacion_detail, name='cotizacion_detail'),

    url(r'^procesados/$',
        views.ProcesadoList.as_view(), name='procesado_list'),

    # reporte de cotizacion
    url(r'^(?P<pk>\d+)/pdf/$', views.CotizacionPDF.as_view(), name='pdf'),
]
