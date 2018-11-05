from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.principal_list, name='principal_list'),

    url(r'^camion/lista/$', views.camion_list, name='camion_list'),
    url(r'^camion/(?P<pk>[0-9]+)/$', views.camion_detail, name='camion_detail'),
    url(r'^camion/(?P<pk>\d+)/remove/$', views.camion_remove, name='camion_remove'),
    url(r'^camion/new/$', views.camion_new, name='camion_new'),
    url(r'^camion/(?P<pk>[0-9]+)/edit/$', views.camion_edit, name='camion_edit'),

    url(r'^piloto/lista/$', views.piloto_list, name='piloto_list'),
    url(r'^piloto/(?P<pk>[0-9]+)/$', views.piloto_detail, name='piloto_detail'),
    url(r'^piloto/(?P<pk>\d+)/remove/$', views.piloto_remove, name='piloto_remove'),
    url(r'^piloto/new/$', views.piloto_new, name='piloto_new'),
    url(r'^piloto/(?P<pk>[0-9]+)/edit/$', views.piloto_edit, name='piloto_edit'),

    url(r'^paquete/$', views.paquete_list, name='paquete_list'),
    url(r'^paquete/(?P<pk>[0-9]+)/$', views.paquete_detail, name='paquete_detail'),
    url(r'^paquete/(?P<pk>\d+)/remove/$', views.paquete_remove, name='paquete_remove'),
    url(r'^paquete/new/$', views.paquete_new, name='paquete_new'),
    url(r'^paquete/(?P<pk>[0-9]+)/edit/$', views.paquete_edit, name='paquete_edit'),

    url(r'^ciudad/lista/$', views.ciudad_list, name='ciudad_list'),
    url(r'^ciudad/nueva/$', views.ciudad_nueva, name='ciudad_nueva'),
    url(r'^ciudad/(?P<pk>\d+)/remove/$', views.ciudad_remove, name='ciudad_remove'),
    #url(r'^camion/nueva/$', views.camion_nueva, name='camion_nueva'),
]
