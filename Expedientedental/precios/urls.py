from django.conf.urls import patterns, url

from precios.views import PreciosGrupos

urlpatterns = patterns(
    'precios.views',

    url(r'^altas/precios/(?P<grupo_id>\d+)/$', 'precios_view', name='precios'),

    url(r'^altas/precios/$', PreciosGrupos.as_view(), name='precios_grupos'),

)
