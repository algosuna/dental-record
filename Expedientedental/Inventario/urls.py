from django.conf.urls import patterns, url
from Inventario.views import Unidad


urlpatterns = patterns('',

    url(r'^unidadades/$', Unidad.as_view()),
)