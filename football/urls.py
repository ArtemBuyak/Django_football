from django.conf.urls import url, include

from football import views


app_name = 'football'
urlpatterns = [
    url(r'^info', views.info, name = 'info'),
    url(r'^', views.start),
]
