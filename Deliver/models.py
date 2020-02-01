from django.db import models
from django.conf import settings


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=-1)
    products = models.TextField()
    amount = models.TextField()


class DeliveryQueue(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_DEFAULT, default=-1)
    location = models.TextField()
    delivery_cost = models.IntegerField()
    done = models.BooleanField(default=False)

    def deliver(self):
        self.done = True
        self.save()
