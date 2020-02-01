import base64

from django.shortcuts import HttpResponse
from .models import Shop, Rate
from django.core.handlers.wsgi import WSGIRequest
from base64 import b64encode
import json


# Create your views here.
def get_shop(request):
    ins = Shop.objects.get(['pk', request.GET.get('pk')])
    ret = {
        'id': ins.id,
        'name': ins.name,
        'background': b64encode(ins.background).decode('ascii'),
        'additions': ins.additions,
        'desc': ins.desc,
        'rate': ins.get_rate(),
        'rates': len(Rate.objects.filter(ref=ins))
    }
    return HttpResponse(json.dumps(ret))


def get_shops(request, start, end):
    list = Shop.objects.all()
    if int(end) >= len(list):
        ret = list[int(start) - 1:int(end)]
    else:
        ret = list[int(start) - 1:]

    ar = []
    for ins in ret:
        map = {
            'id': ins.id,
            'name': ins.name,
            'background': b64encode(ins.background).decode('ascii'),
            'email': ins.email,
            'phone_no': ins.phone_no,
            'rate': ins.get_rate(),
            'desc': ins.desc,
            'rates': len(Rate.objects.filter(ref=ins))
        }
        ar.append(map)
    return HttpResponse(json.dumps(ar))


def delete(request, pk):
    ins = Shop.objects.get(['pk', pk])
    ins.delete()
    return HttpResponse(0)


def by_name(request):
    ins = None
    try:
        ins = Shop.objects.get(['name', request.GET.get('name')])
        map = {
            'id': ins.id,
            'name': ins.name,
            'background': b64encode(ins.background).decode('ascii'),
            'email': ins.email,
            'phone_no': ins.phone_no,
            'rate': ins.get_rate(),
            'desc': ins.desc,
            'rates': len(Rate.objects.filter(ref=ins))
        }
        return HttpResponse(json.dumps(map))
    except Exception as e:
        p = e
    return HttpResponse(p)


def get_count(request):
    return HttpResponse(Shop.objects.count())


def create(request):
    body = json.loads(request.body.decode('UTF-8'))
    # base64.b64decode()
    try:
        Shop.objects.create(name=body['name'], additions=body['add'],
                            start_hour=body['start_hour'],
                            end_hour=body['end_hour'],
                            phone_no=body['phone'],
                            email=body['email'],
                            background=base64.b64decode(body['img']), desc=json.dumps(body['desc']))
        return HttpResponse('0')
    except Exception as e:
        print(e)
        return HttpResponse('1')
        return


def rate(request):
    try:
        Rate.objets.create(ref=Shop.objects.get(['id', request.GET.get('id')]), rate=request.GET.get('rate')).save()
        return HttpResponse('done')
    except Exception:
        return HttpResponse('done')
