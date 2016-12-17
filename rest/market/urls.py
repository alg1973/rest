from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<rest_id>[0-9]+)/$', views.menu, name='menu'),
    url(r'^account/$', views.account, name='account'),
    url(r'^basket/$', views.basket, name='basket'),
    url(r'^account/(?P<rest_id>[0-9]+)/$', views.account, name='account'),
]
