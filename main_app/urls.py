from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cars/', views.cars_index, name='all_cars'),
    path('bookings/', views.bookings_index, name='all_bookings'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/<int:car_id>/add_booking/', views.add_booking, name='add_booking'),
    path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
    path('bookings/<int:pk>/delete/', views.BookingDelete.as_view(), name='cancel_booking'),
    path('bookings/<int:pk>/update/', views.BookingUpdate.as_view(), name='edit_booking')
]
