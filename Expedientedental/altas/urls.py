from django.conf.urls import patterns, url
from altas.views import GrupoNewView, GruposView, GrupoUpdateView, Medicos,\
    MedicoCreate, MedicoUpdate, TratamientoNewView, TratamientoUpdateView,\
    TratamientosView, Pacientes, PacienteUpdate, PacienteCreate,\
    EvaluacionNewView, EvaluacionUpdateView, EvaluacionesView,\
    TratamientoPreventivoNewView, TratamientoPreventivoUpdateView,\
    TratamientosPreventivosView

urlpatterns = patterns(
    'altas.views',

    url(r'^medicos/$', Medicos.as_view(), name='medicos'),
    url(r'^medico/new/$', MedicoCreate.as_view(), name='medico_new'),
    url(r'^medico/edit/(?P<pk>\d+)/$',
        MedicoUpdate.as_view(), name='medico_edit'),

    url(r'^pacientes/$', Pacientes.as_view(), name='pacientes'),
    url(r'^paciente/new/$', PacienteCreate.as_view()),
    url(r'^paciente/edit/(?P<pk>\d+)/$', PacienteUpdate.as_view()),

    url(r'^grupos/$', GruposView.as_view(), name='grupos'),
    url(r'^grupo/new/$', GrupoNewView.as_view(), name='grupo_new'),
    url(r'^grupo/edit/(?P<pk>\d+)/$',
        GrupoUpdateView.as_view(), name='grupo_edit'),

    url(r'^tratamiento/$', TratamientosView.as_view()),
    url(r'^tratamiento/new/$', TratamientoNewView.as_view()),
    url(r'^tratamiento/edit/(?P<pk>\d+)/$',
        TratamientoUpdateView.as_view()),

    url(r'^evaluacion/$', EvaluacionesView.as_view()),
    url(r'^evaluacion/new/$', EvaluacionNewView.as_view()),
    url(r'^evaluacion/edit/(?P<pk>\d+)/$',
        EvaluacionUpdateView.as_view()),

    url(r'^preventivo/$', TratamientosPreventivosView.as_view()),
    url(r'^preventivo/new/$', TratamientoPreventivoNewView.as_view()),
    url(r'^preventivo/edit/(?P<pk>\d+)/$',
        TratamientoPreventivoUpdateView.as_view()),
)
