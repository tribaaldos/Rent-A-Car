from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cars/', views.cars_index, name='all_cars'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/<int:car_id>/add_booking/',
         views.add_booking, name='add_booking'),
]
