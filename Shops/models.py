from django.db import models
from django.core import serializers


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=300)
    background = models.BinaryField()
    desc = models.TextField()
    additions = models.TextField()

    def get_rate(self) -> float:
        list = Rate.objects.filter(ref=self)
        if len(list) == 0:
            return None
        else:
            tot = 0
            for r in list:
                tot += r.rate
            return tot / len(list)


class Rate(models.Model):
    ref = models.ForeignKey(Shop, on_delete=models.CASCADE)
    rate = models.FloatField(null=False)
