from django.conf.urls import url, include

from football import views


app_name = 'football'
urlpatterns = [
    url(r'^info', views.info, name = 'info'),
    url(r'^tournament/(?P<tournament_id>[0-9]+)', views.tournament, name = "tournament"),
    url(r'^tournaments', views.tournaments, name = "tournaments"),
    url(r'^registration_to_cup/(?P<tournament_id>[0-9]+)', views.registration, name= "registration"),
    url(r'^', views.start, name='main'),
]
