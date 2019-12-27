"""Back_End URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from json import loads


def is_Admin(name, passwd):
    case = 2
    try:
        user = User.objects.get(['username', name])
        case = 1
        if user.check_password(passwd):
            case = 0
    except Exception as e:
        print(e)
        pass
    return case


def is_admin(request):
    content = loads(request.body.decode('utf-8'))
    name = content['name']
    passwd = content['pass']
    case = 2
    try:
        user = User.objects.get(['username', name])
        case = 1
        if user.check_password(passwd):
            case = 0
    except Exception:
        pass
    return HttpResponse(case)


urlpatterns = [
    path('admin/', admin.site.urls),
    url('shops/', include('Shops.urls')),
    url('products/', include('Products.urls')),
    url('deliver/', include('Deliver.urls')),
    url('isAdmin', is_admin)
]
