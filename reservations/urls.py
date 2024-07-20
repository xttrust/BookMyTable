from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),  # URL for viewing reservations
    path('reserve/', views.reserve_table, name='reserve_table'),  # URL for making a reservation
    path('success/', views.reservation_success, name='reservation_success'),  # URL for success page
]
