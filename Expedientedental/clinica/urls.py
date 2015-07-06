from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.paciente_search, name='paciente_search'),

    url(r'^(?P<paciente_id>\d+)/odontograma/$',
        views.odontograma, name='odontograma'),

    url(r'^procedimiento/(?P<procedimiento_id>\d+)/$',
        views.bitacora_create, name='bitacora_create'),

    url(r'^(?P<pk>\d+)/detail/$',
        views.PacienteDetail.as_view(), name='paciente_detail'),

    url(r'^odontograma/(?P<pk>\d+)/detail/$',
        views.OdontogramaDetail.as_view(), name='odontograma_detail'),

    url(r'^procedimientos/(?P<pk>\d+)/$',
        views.ProcedimientosView.as_view(), name='procedimientos'),

    url(r'^historial/(?P<pk>\d+)/$',
        views.HistorialView.as_view(), name='historial'),

    url(r'^historial/procedimiento/(?P<pk>\d+)/$',
        views.HistorialDetail.as_view(), name='historial_detail'),

    url(r'^interrogatorio/(?P<pk>\d+)/$',
        views.InterrogatorioView.as_view(), name='interrogatorio'),

    url(r'^(?P<pk>\d+)/radiografias/$',
        views.Radiografias.as_view(), name='radiografias'),

    url(r'^(?P<pk>\d+)/radiografia/new/$',
        views.RadiografiaCreate.as_view(), name='radiografia_create'),

    url(r'^radiografia/(?P<pk>\d+)/detail/$',
        views.RadiografiaDetail.as_view(), name='radiografia_detail'),

    url(r'^radiografia/(?P<pk>\d+)/update/$',
        views.RadiografiaUpdate.as_view(), name='radiografia_update'),

    # Reportes PDF
    url(r'^interrogatorio/(?P<paciente_id>\d+)/pdf/$',
        views.InterrogatorioPDF.as_view(), name='pdf'),
]
