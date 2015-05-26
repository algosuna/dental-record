from django.conf.urls import patterns, url
from utilidad.views import dolarCreate

urlpatterns = patterns(
    'utilidad.views',

    url(r'^divisas/$', dolarCreate.as_view()),
    )