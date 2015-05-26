from django.conf.urls import patterns, url

urlpatterns = patterns(
    'utilidad.views',

    url(r'^$', 'algo', name='algo'),

)
