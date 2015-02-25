from django.conf.urls import patterns, url

urlpatterns = patterns('ActividadesClinicas.views',

    url(r'^$', 'index'),
    url(r'^interrogatorio/$', 'HistoriaClinica'),
    url(r'^odontograma/$', 'odontograma'),
    url(r'^diagnosticos/$', 'diagnosticos'),

)
