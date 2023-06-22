from django.forms import ModelForm
from .models import Booking, Review
from django import forms

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['trip_start', 'trip_end']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
