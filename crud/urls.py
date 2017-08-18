from django.conf.urls import url
from crud.views import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^insert/$', views.insert, name='insert'),
    url(r'^delete/(?P<user_id>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<user_id>\d+)$', views.edit, name='edit')
]