from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^postScore/$', views.postScore, name='postScore'),
    url(r'^postName/$', views.postName, name='postName'),
]
