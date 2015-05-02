from django.conf.urls import patterns, url

from accounts.views import LoginView, HomeView


urlpatterns = patterns(
    'accounts.views',

    url(r'^logout/$', 'logout_view', name='logout'),

)

urlpatterns += patterns(
    '',

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', HomeView.as_view(), name='home'),
)
