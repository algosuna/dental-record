from django.conf.urls import patterns, url
from calculos.views import dolarCreate

urlpatterns = patterns(
    'calculos.views',

    url(r'^divisas/$', dolarCreate.as_view()),
    )