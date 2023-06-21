from django.db import models
from django.urls import reverse
import random
from django.contrib.auth.models import User

# Create your models here.


class Car(models.Model):
    brand = models.CharField(default="", max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.IntegerField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} ${self.price_per_day}'


class Booking(models.Model):
    trip_start = models.DateField('Booking Date')
    trip_end = models.DateField()
    # booking_num = random.randint(111111111, 999999999)
    booking_number = models.AutoField(primary_key=True)
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.trip_start}-{self.trip_end} #booking {self.booking_number}"

    def get_absolute_url(self):
        return reverse('all_bookings', )
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)