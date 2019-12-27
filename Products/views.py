from django.shortcuts import HttpResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import base64


# Create your views here.
def range(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    ar = []
    for ins in Product.objects.filter(id__gte=start, id__lte=end):
        ar.append(ins.get_dict())
    return HttpResponse(json.dumps(ar))


def code(request, code):
    return HttpResponse('passed')


def get_count(request):
    return HttpResponse(Product.objects.count())


def create(request):
    body = json.loads(request.body.decode('UTF-8'))
    # base64.b64decode()
    Product.objects.create(name=body['name'], cost=body['cost'], code=body['code'], manufacture=body['manufacture'],
                           image=base64.b64decode(body['image']), desc=body['desc'])
    return HttpResponse('done')


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
