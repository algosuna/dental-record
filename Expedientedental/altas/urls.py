from django.conf.urls import patterns,url
from altas.views import GrupoNewView, GruposView, GrupoUpdateView

urlpatterns = patterns('altas.views',

	url(r'^medicos/$','datosmedico_view', name='datosmedico'),
	url(r'^pacientes/$','datospaciente_view', name='datospaciente'),
    url(r'^grupo/new/$', GrupoNewView.as_view(), name='grupo-new'),
    url(r'^grupos/$', GruposView.as_view(), name='grupos'),
    url(r'^grupo/edit/(?P<pk>\d+)/$', GrupoUpdateView.as_view(), name='grupo-edit'),
)


