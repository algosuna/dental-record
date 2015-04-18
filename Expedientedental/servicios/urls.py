from django.conf.urls import patterns, url

from servicios.views import PaqueteList, PaqueteDetail

urlpatterns = patterns(
    'servicios.views',

    url(r'^servicios/create/(?P<cotizacion_id>\d+)/$', 'servicios_create'),
    url(r'^servicios/paquetes/$', PaqueteList.as_view()),
    url(r'^servicios/detail/(?P<pk>\d+)/$', PaqueteDetail.as_view()),

)
