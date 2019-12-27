from django.shortcuts import HttpResponse
from .models import Shop, Rate
from django.core.handlers.wsgi import WSGIRequest
from base64 import b64encode
import json


# Create your views here.
def get_shop(request, pk):
    ins = Shop.objects.get(['pk', pk])
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


def get_shops(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    ret = Shop.objects.filter(id__gte=start, id__lte=end)
    ar = []
    for ins in ret:
        map = {
            'id': ins.id,
            'name': ins.name,
            'background': b64encode(ins.background).decode('ascii'),
            'additions': ins.additions,
            'desc': ins.desc,
            'rate': ins.get_rate(),
            'rates': len(Rate.objects.filter(ref=ins))
        }
        ar.append(map)
    return HttpResponse(json.dumps(ar))


def get_count(request):
    return HttpResponse(Shop.objects.count())


def create(request: WSGIRequest):
    return HttpResponse(str(type(request)));


def rate(request):
    try:
        Rate.objets.create(ref=Shop.objects.get(['id', request.GET.get('id')]), rate=request.GET.get('rate')).save()
        return HttpResponse('done')
    except Exception:
        return HttpResponse('done')
