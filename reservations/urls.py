from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('reserve/', views.reserve_table, name='reserve_table'),
    path('success/', views.reservation_success, name='reservation_success'),
    path('edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]
