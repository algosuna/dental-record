from django.conf.urls import patterns, url
from pagos.views import RecibodePagoPDF

urlpatterns = patterns(
    'pagos.views',

    url(r'^$', 'paciente_search', name='paciente_search'),
    url(r'^list/$', 'pagos_list', name='pagos_list'),

    url(r'^list/(?P<paciente_id>\d+)/$',
        'pagos_paciente', name='pagos_paciente'),

    url(r'^pending/(?P<paciente_id>\d+)/$',
        'pagos_pending', name='pagos_pending'),

    # apply payment by paquete
    url(r'^(?P<paquete_id>\d+)/$', 'pagos', name='pagar'),

    # patment detail
    url(r'^detalle/(?P<pago_id>\d+)/$', 'pagos_detail', name='pagos_detail'),
    )


urlpatterns += patterns(
    '',

    url(r'^pago/(?P<pago_id>\d+)/pdf/$', RecibodePagoPDF.as_view()),
)
