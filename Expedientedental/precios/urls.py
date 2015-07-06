from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^altas/precios/(?P<grupo_id>\d+)/$',
        views.precios_view, name='precios'),
    url(r'^altas/precios/$',
        views.PreciosGrupos.as_view(), name='precios_grupos'),
]
