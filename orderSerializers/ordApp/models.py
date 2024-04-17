from django.db import models

# Create your models here.


class Custumer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)


class Order(models.Model):
    product = models.CharField(max_length=30)
    quantity = models.IntegerField()
    custumer = models.ForeignKey(
        Custumer, related_name="order", on_delete=models.CASCADE
    )
