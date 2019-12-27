from django.db import models
from base64 import b64encode


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    cost = models.IntegerField()
    code = models.CharField(max_length=2057, unique=True)
    manufacture = models.CharField(max_length=100)
    image = models.BinaryField()
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_dict(self):
        dic = {
            'id': self.id,
            'name': self.name,
            'cost': self.cost,
            'image': b64encode(self.image).decode('ascii'),
            'desc': self.desc,
            'rate': self.get_rate(),
            'rates': self.get_rates()
        }
        return dic

    def get_rate(self) -> float:
        list = Rate.objects.filter(ref=self)
        if len(list) == 0:
            return None
        else:
            tot = 0
            for r in list:
                tot += r.rate
            return tot / len(list)

    def get_rates(self):
        return len(Rate.objects.filter(ref=self))

    def sell(self, amount: int):
        if amount > self.store:
            raise Exception('there is no enough {self.name} to complete this operation')
        self.store = self.store - amount
        self.save()

    def add(self, amount: int):
        self.store = self.store + amount
        self.save()


class Rate(models.Model):
    ref = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.FloatField(null=False)
