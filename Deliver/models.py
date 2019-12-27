from django.db import models


# Create your models here.
class DeliveryQueue(models.Model):
    name = models.CharField(max_length=300)
    location = models.TextField()
    delivery_cost = models.IntegerField()
    done = models.BooleanField(default=False)

    def deliver(self):
        self.done = True
        self.save()

class Cart(models.Model):
    pass