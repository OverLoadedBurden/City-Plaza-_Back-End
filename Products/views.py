from django.shortcuts import HttpResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import base64


# Create your views here.
def range(request, start, end):
    list = Product.objects.all()
    if int(end) >= len(list):
        ret = list[int(start) - 1:int(end)]
    else:
        ret = list[int(start) - 1:]
    ar = []
    for ins in ret:
        ar.append(ins.get_dict())
    return HttpResponse(json.dumps(ar))


def code(request):
    code = request.GET.get('code')
    p = Product.objects.get(['code', code])
    return HttpResponse(json.dumps(p.get_dict()))


def delete(request, pk):
    p = Product.objects.get(['pk', int(pk)])
    p.delete()
    return HttpResponse('0')


def get_count(request):
    return HttpResponse(Product.objects.count())


def create(request):
    body = json.loads(request.body.decode('UTF-8'))
    # base64.b64decode()
    Product.objects.create(name=body['name'], cost=body['cost'], code=body['code'], manufacture=body['manufacture'],
                           image=base64.b64decode(body['image']), desc=body['desc'])
    return HttpResponse(0)


method_decorator(csrf_protect)


def rate(request):
    id = request.GET.get('id')
    rate = request.GET.get('rate')
    Rate.objects.create(ref=Product.objects.get(['id', id]), rate=rate).save()
    return HttpResponse('Done')


def by_name(request):
    p = None
    try:
        p = Product.objects.get(['name', request.GET.get('name')])
        p = json.dumps(p.get_dict())
    except Exception as e:
        p = e
    return HttpResponse(p)
