from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<user_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<user_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^new/$', views.new, name='new'),
    url(r'^export/$', views.export, name='export'),
]
