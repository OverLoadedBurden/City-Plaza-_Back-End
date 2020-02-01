from django.conf.urls import url
from .views import *

urlpatterns = [
    url('count', get_count),
    url(r'^get/', get_shop),
    url(r'^del/(?P<pk>\d)/$', delete),
    url(r'^range/(?P<start>\d)/(?P<end>\d)/$', get_shops),
    url('create/', create),
    url(r'^byName/', by_name),
    url('rate/', rate)
]
