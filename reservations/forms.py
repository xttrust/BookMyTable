from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'email', 'phone', 'reservation_date', 'number_of_people', 'special_requests']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'reservation_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of People'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Special Requests'}),
        }
