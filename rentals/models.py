from django.db import models
from cars.models import Car
from clients.models import Client

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    start_date = models.DateField()

    end_date = models.DateField(null=True, blank=True)

    weekly_price = models.DecimalField(max_digits=8, decimal_places=2)

    paid = models.BooleanField(default=True)

    km_start = models.IntegerField()

    km_end = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.car} alugado por {self.client}"
