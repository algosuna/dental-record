from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^medicos/$', views.Medicos.as_view(), name='medicos'),
    url(r'^medico/new/$', views.medico_create, name='medico_new'),
    url(r'^medico/edit/(?P<pk>\d+)/$',
        views.MedicoUpdate.as_view(), name='medico_edit'),

    url(r'^pacientes/$', views.Pacientes.as_view(), name='pacientes'),
    url(r'^paciente/new/$',
        views.PacienteCreate.as_view(), name='paciente_new'),
    url(r'^paciente/edit/(?P<pk>\d+)/$',
        views.PacienteUpdate.as_view(), name='paciente_edit'),

    url(r'^grupos/$', views.GruposView.as_view(), name='grupos'),
    url(r'^grupo/new/$', views.GrupoNewView.as_view(), name='grupo_new'),
    url(r'^grupo/edit/(?P<pk>\d+)/$',
        views.GrupoUpdateView.as_view(), name='grupo_edit'),

    url(r'^tratamiento/$',
        views.TratamientosView.as_view(), name='tratamiento'),
    url(r'^tratamiento/new/$',
        views.TratamientoNewView.as_view(), name='tratamiento_new'),
    url(r'^tratamiento/edit/(?P<pk>\d+)/$',
        views.TratamientoUpdateView.as_view(), name='tratamiento_edit'),

    url(r'^evaluacion/$', views.EvaluacionesView.as_view(), name='evaluacion'),
    url(r'^evaluacion/new/$',
        views.EvaluacionNewView.as_view(), name='evaluacion_new'),
    url(r'^evaluacion/edit/(?P<pk>\d+)/$',
        views.EvaluacionUpdateView.as_view(), name='evaluacion_edit'),

    url(r'^preventivo/$',
        views.TratamientosPreventivosView.as_view(), name='preventivo'),
    url(r'^preventivo/new/$',
        views.TratamientoPreventivoNewView.as_view(), name='preventivo_new'),
    url(r'^preventivo/edit/(?P<pk>\d+)/$',
        views.TratamientoPreventivoUpdate.as_view(), name='preventivo_edit'),
]
