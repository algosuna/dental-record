from django.conf.urls import patterns, url
from pagos.views import RecibodePagoPDF, PagosPacienteList, PagosDetail,\
    PagosPending

urlpatterns = patterns(
    'pagos.views',

    url(r'^$', 'paciente_search', name='paciente_search'),
    url(r'^list/$', 'pagos_list', name='pagos_list'),

    # apply payment by paquete
    url(r'^(?P<paquete_id>\d+)/$', 'pagos', name='pagar'),

)

urlpatterns += patterns(
    '',

    url(r'^pending/(?P<pk>\d+)/$',
        PagosPending.as_view(), name='pagos_pending'),

    # patment detail
    url(r'^detail/(?P<pk>\d+)/$', PagosDetail.as_view(), name='pagos_detail'),

    url(r'^list/(?P<pk>\d+)/$',
        PagosPacienteList.as_view(), name='pagos_paciente'),

    url(r'^pago/(?P<pago_id>\d+)/pdf/$', RecibodePagoPDF.as_view()),
)
