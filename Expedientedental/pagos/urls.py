from django.conf.urls import patterns, url

urlpatterns = patterns(
    'pagos.views',

    url(r'^$', 'paciente_search'),
    url(r'^list/$', 'pagos_list'),
    url(r'^list/(?P<paciente_id>\d+)/$', 'pagos_paciente'),
    url(r'^pending/(?P<paciente_id>\d+)/$', 'pagos_pending'),

    # apply payment by cotizacion
    url(r'^(?P<cotizacion_id>\d+)/$', 'pagos'),

    # patment detail
    url(r'^detalle/(?P<pago_id>\d+)/$', 'pagos_detail', name='pagos_detail')

)
