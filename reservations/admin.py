from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'reservation_date', 'number_of_people', 'phone')
    list_filter = ('reservation_date', 'number_of_people')
    search_fields = ('full_name', 'email', 'phone')
