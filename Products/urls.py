from django.conf.urls import url
from .views import *

urlpatterns = [
    url('range/', range),
    url(r'^code/(?P<code>)\s/$', code),
    url('create/', create),
    url('count', get_count),
    url(r'^rate/', rate),
    url(r'^byName/', by_name)
]
