from django.conf.urls import url
from .views import *

urlpatterns = [
    url('count', get_count),
    url(r'^get/(?P<pk>\d)/$', get_shop),
    url(r'range/', get_shops),
    url('create/', create),
    url('rate/',rate)
]
