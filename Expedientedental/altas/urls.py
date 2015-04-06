from django.conf.urls import patterns, url
from altas.views import GrupoNewView, GruposView, GrupoUpdateView, Medicos,\
    MedicoCreate, MedicoUpdate, TratamientoNewView, TratamientoUpdateView,\
    TratamientosView, Pacientes, PacienteUpdate, PacienteCreate,\
    EvaluacionNewView, EvaluacionUpdateView, EvaluacionesView,\
    TratamientoPreventivoNewView, TratamientoPreventivoUpdateView,\
    TratamientosPreventivosView

urlpatterns = patterns(
    'altas.views',

    url(r'^medicos/$', Medicos.as_view()),
    url(r'^medico/new/$', MedicoCreate.as_view()),
    url(r'^medico/edit/(?P<pk>\d+)/$', MedicoUpdate.as_view()),

    url(r'^pacientes/$', Pacientes.as_view()),
    url(r'^paciente/new/$', PacienteCreate.as_view()),
    url(r'^paciente/edit/(?P<pk>\d+)/$', PacienteUpdate.as_view()),

    url(r'^grupo/new/$', GrupoNewView.as_view()),
    url(r'^grupos/$', GruposView.as_view()),
    url(r'^grupo/edit/(?P<pk>\d+)/$', GrupoUpdateView.as_view()),

    url(r'^tratamiento/new/$', TratamientoNewView.as_view()),
    url(r'^tratamiento/edit/(?P<pk>\d+)/$',
        TratamientoUpdateView.as_view()),
    url(r'^tratamiento/$', TratamientosView.as_view()),

    url(r'^evaluacion/new/$', EvaluacionNewView.as_view()),
    url(r'^evaluacion/edit/(?P<pk>\d+)/$',
        EvaluacionUpdateView.as_view()),
    url(r'^evaluacion/$', EvaluacionesView.as_view()),

    url(r'^preventivo/new/$', TratamientoPreventivoNewView.as_view()),
    url(r'^preventivo/edit/(?P<pk>\d+)/$',
        TratamientoPreventivoUpdateView.as_view()),
    url(r'^preventivo/$', TratamientosPreventivosView.as_view()),
)
