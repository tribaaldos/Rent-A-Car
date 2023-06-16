from django.db import models

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.IntegerField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} ${self.price_per_day}'
