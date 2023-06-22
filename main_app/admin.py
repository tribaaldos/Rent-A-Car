from django.contrib import admin
from .models import Car, Booking, Photo, Review

# Register your models here.

admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(Photo)
admin.site.register(Review)