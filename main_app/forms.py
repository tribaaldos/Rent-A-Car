from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['trip_start', 'trip_end', 'car', 'booking_number']
