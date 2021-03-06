

from django.shortcuts import render
from django.conf.urls import url
from blog import views



urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^article/(?P<id_article>\d+)$', views.view_article, name="afficher_article"),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),
    url(r'^redirection$', views.view_redirection),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
]
