from django.conf.urls import patterns, url

from utilidad.views import ServiciosPaciente, UtilidadServicio, paciente_search


urlpatterns = patterns(
    '',

    url(r'^search/$', paciente_search, name='utilidad_search'),

    url(r'^paciente/(?P<pk>\d+)/$',
        ServiciosPaciente.as_view(), name='utilidad_servicios'),

    url(r'^servicio/(?P<pk>\d+)/$',
        UtilidadServicio.as_view(), name='utilidad_servicio')

)
