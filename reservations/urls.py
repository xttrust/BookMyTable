# reservations/urls.py
from django.urls import path
from . import views

app_name = 'reservations'  
urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('reserve/', views.reserve_table, name='reserve_table'),  # Correct URL name
    path('success/', views.reservation_success, name='reservation_success'),
]
