from django.conf.urls import patterns, url

urlpatterns = patterns('paquete.views',

    url(r'^paquete/$', 'paquete'),
    url(r'^tipoPaquete/$', 'tipoPaquete'),

)