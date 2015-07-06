from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^search/$', views.paciente_search, name='utilidad_search'),

    url(r'^paciente/(?P<pk>\d+)/$',
        views.ServiciosPaciente.as_view(), name='utilidad_servicios'),

    url(r'^servicio/(?P<pk>\d+)/$',
        views.UtilidadServicio.as_view(), name='utilidad_servicio')
]
