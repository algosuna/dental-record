from django.conf.urls import patterns, url
from pagos.views import (
    RecibodePagoPDF, PagosPacienteList, PagosDetail, PagosPending,
    PagosServicio, PagosServicios, HistorialPagosPDF, PagosCotizacionList
)

urlpatterns = patterns(
    'pagos.views',

    url(r'^$', 'paciente_search', name='paciente_search'),
    url(r'^list/$', 'pagos_list', name='pagos_list'),

    # apply payment by paquete
    url(r'^(?P<paquete_id>\d+)/$', 'pagos', name='pagar'),

)

urlpatterns += patterns(
    '',

    url(r'^(?P<pk>\d+)/pending/$',
        PagosPending.as_view(), name='pagos_pending'),

    # payment detail
    url(r'^(?P<pk>\d+)/detail/$', PagosDetail.as_view(), name='pagos_detail'),

    url(r'^list/(?P<pk>\d+)/$',
        PagosPacienteList.as_view(), name='pagos_paciente'),

    url(r'^cotizacion/(?P<pk>\d+)/$',
        PagosCotizacionList.as_view(), name='pagos_cotizacion'),

    url(r'^servicios/(?P<pk>\d+)/$',
        PagosServicios.as_view(), name='pagos_servicios'),

    url(r'^servicio/(?P<pk>\d+)/$',
        PagosServicio.as_view(), name='pagos_servicio'),

    # url(r'^pago/(?P<pago_id>\d+)/pdf/$', RecibodePagoPDF.as_view()),

    url(r'^paquete/recibo/pdf/$',
        HistorialPagosPDF.as_view(), name='historial'),

    url(r'^pago/(?P<pago_id>\d+)/pdf/$', RecibodePagoPDF.as_view(),
        name='pdf'),
)
