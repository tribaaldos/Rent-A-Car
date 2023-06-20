from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Car, Booking
from .forms import BookingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def bookings_index(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/index.html', {'bookings': bookings})


def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)

    booking_form = BookingForm()

    return render(request, 'cars/detail.html', {
        'car': car, 'booking_form': booking_form
    })


def add_booking(request, car_id):
    form = BookingForm(request.POST)
    if form.is_valid():
        # We want a model instance, but
        # we can't save to the db yet
        # because we have not assigned the
        # cat_id FK.
        new_booking = form.save(commit=False)
        new_booking.user = request.user
        new_booking.car_id = car_id
        new_booking.save()
    return redirect('detail', car_id=car_id)


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
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
