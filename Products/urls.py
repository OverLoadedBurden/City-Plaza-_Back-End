from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^range/(?P<start>\d)/(?P<end>\d)/$', range),
    url(r'^code/', code),
    url(r'^del/(?P<pk>\d)/$', delete),
    url('create/', create),
    url('count', get_count),
    url(r'^rate/', rate),
    url(r'^byName/', by_name)
]
