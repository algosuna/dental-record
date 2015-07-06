from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.paciente_search, name='paciente_search'),
    url(r'^list/$', views.pagos_list, name='pagos_list'),

    # apply payment by paquete
    url(r'^(?P<paquete_id>\d+)/$', views.pagos, name='pagar'),

    url(r'^(?P<pk>\d+)/pending/$',
        views.PagosPending.as_view(), name='pagos_pending'),

    # payment detail
    url(r'^(?P<pk>\d+)/detail/$',
        views.PagosDetail.as_view(), name='pagos_detail'),

    url(r'^list/(?P<pk>\d+)/$',
        views.PagosPacienteList.as_view(), name='pagos_paciente'),

    url(r'^cotizacion/(?P<pk>\d+)/$',
        views.PagosCotizacionList.as_view(), name='pagos_cotizacion'),

    url(r'^servicios/(?P<pk>\d+)/$',
        views.PagosServicios.as_view(), name='pagos_servicios'),

    url(r'^servicio/(?P<pk>\d+)/$',
        views.PagosServicio.as_view(), name='pagos_servicio'),

    # url(r'^pago/(?P<pago_id>\d+)/pdf/$', RecibodePagoPDF.as_view()),

    url(r'^paquete/recibo/pdf/$',
        views.HistorialPagosPDF.as_view(), name='historial'),

    url(r'^pago/(?P<pago_id>\d+)/pdf/$',
        views.RecibodePagoPDF.as_view(), name='pdf'),
]
