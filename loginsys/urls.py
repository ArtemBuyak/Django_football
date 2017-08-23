from django.conf.urls import url, include

from loginsys import views

app_name = "loginsys"
urlpatterns = [
    url(r'^login/', views.login, name = 'login'),
    url(r'^logout/', views.logout, name = 'logout'),
]