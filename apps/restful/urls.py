from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'users/$', views.home),
    url(r'(?P<id>\d+)$', views.view),
    url(r'new$', views.new),
    url(r'(?P<id>\d+)/edit$', views.edit),
    url(r'create$', views.create),
    url(r'(?P<id>\d+)/update$', views.update),
    url(r'(?P<id>\d+)/delete$', views.delete)
]