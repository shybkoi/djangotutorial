from django.conf.urls import patterns, url
from nine import views


urlpatterns = patterns(
    '',
    url(r'^square', views.square),
    url(r'^heroes/$', views.heroes),
    url(r'^heroes/(?P<heroes_nik>\w+)/$', views.heroes),
)
