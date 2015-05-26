from django.conf.urls import patterns, url

urlpatterns = patterns(
    'servicios.views',

    url(r'^servicios/create/(?P<cotizacion_id>\d+)/$',
        'servicios_create', name='servicios_create'),

)
