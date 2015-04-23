from django.conf.urls import patterns, url


urlpatterns = patterns(
    'accounts.urls',

    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
    url(r'^home/$', 'home'),
    url(r'^password/change/$', 'password_change'),

)
