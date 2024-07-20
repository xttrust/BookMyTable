from django.db import models
from django.conf import settings
from django.utils import timezone
from table.models import Table  

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_people = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reservation by {self.full_name} on {self.reservation_date} at {self.reservation_time}"
