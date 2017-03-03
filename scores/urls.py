from django.conf.urls import url
from . import views

urlpatterns = [
    ##url(r'^getHighscores/$', views.getHighscores, name='getHighscores'),
    url(r'^postScore/$', views.postScore, name='postScore')
]
