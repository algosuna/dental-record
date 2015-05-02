from django.conf.urls import patterns, url
from calculos.views import dolar

urlpatterns = patterns(
    'calculos.views',

    url(r'^divisas/$', dolar),
    )