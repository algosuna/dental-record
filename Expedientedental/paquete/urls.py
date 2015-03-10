from django.conf.urls import patterns, url
from paquete.views import PaquetesPDF

urlpatterns = patterns('paquete.views',

    url(r'^paquete/$', 'paquete'),
    url(r'^tipoPaquete/$', 'tipoPaquete'),

)

urlpatterns += patterns('',

    #Reportes PDF
    url(r'^paquetes/pdf/$',PaquetesPDF.as_view()),
)
