from django.conf.urls import patterns, url

urlpatterns = patterns(
    'pagos.views',


    url(r'^$', 'pagos_list'),
    url(r'^(?P<cotizacion_id>\d+)/$', 'pagos'),
    url(r'^detalle/(?P<pago_id>\d+)/$', 'pagos_detail', name='pagos_detail'),
    url(r'^pendientes/$', 'pagos_pending', name='pagos_pending'),

)
