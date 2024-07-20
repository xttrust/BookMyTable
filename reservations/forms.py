# reservations/forms.py

from django import forms
from .models import Reservation
from table.models import Table
from datetime import time

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'email', 'phone', 'reservation_date', 'reservation_time', 'number_of_people', 'special_requests', 'table']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'reservation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Reservation Date'}),
            'reservation_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'Reservation Time'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of People'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Special Requests'}),
            'table': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_reservation_time(self):
        reservation_time = self.cleaned_data['reservation_time']
        start_time = time(8, 0)  # 8 AM
        end_time = time(21, 0)  # 9 PM

        if not (start_time <= reservation_time <= end_time):
            raise forms.ValidationError(f"Reservation time must be between {start_time.strftime('%H:%M')} and {end_time.strftime('%H:%M')}.")
        
        return reservation_time
