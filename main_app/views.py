import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from .models import Car, Booking, Photo
from .forms import BookingForm
from datetime import date, datetime

# Create your views here.


def home(request):
    return render(request, 'home.html')


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def bookings_index(request):
    bookings = Booking.objects.filter(user=request.user)
    past_bookings = []
    current_bookings = []
    for booking in bookings:
        if booking.trip_end < date.today():
            past_bookings.append(booking)
        else:
            current_bookings.append(booking)
    return render(request, 'bookings/index.html', {
        'past_bookings': past_bookings,
        'current_bookings': current_bookings,
    })


def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)

    booking_form = BookingForm()

    return render(request, 'cars/detail.html', {
        'car': car, 'booking_form': booking_form, 'is_valid_date': True
    })


def add_booking(request, car_id):
    car = Car.objects.get(id=car_id)
    booking_form = BookingForm()
    form = BookingForm(request.POST)
    date_format = '%Y-%m-%d'
    # We can't choose past dates
    if datetime.strptime(request.POST['trip_start'], date_format).date() < date.today() or datetime.strptime(request.POST['trip_end'], date_format).date() < date.today():
        return render(request, 'cars/detail.html',
                      {'car': car, 'booking_form': booking_form, 'is_valid_date': False})
    # End date can't be before the start date
    if datetime.strptime(request.POST['trip_start'], date_format) > datetime.strptime(request.POST['trip_end'], date_format):
        return render(request, 'cars/detail.html',
                      {'car': car, 'booking_form': booking_form, 'is_valid_date': False})
    # if someone already booked the date, you can't book that date
    if form.is_valid():
        # We want a model instance, but
        # we can't save to the db yet
        # because we have not assigned the
        # cat_id FK.
        new_booking = form.save(commit=False)
        new_booking.user = request.user
        new_booking.car_id = car_id
        new_booking.save()
    return redirect('all_bookings')


class BookingUpdate(UpdateView):
    model = Booking
    fields = ['trip_start', 'trip_end']


class BookingDelete (DeleteView):
    model = Booking
    success_url = '/bookings'


def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}/{bucket}/{key}"
            Photo.objects.create(url=url, car_id=car_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('all_cars',)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
