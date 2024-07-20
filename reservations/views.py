# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm

@login_required
def reservation_list(request):
    reservations = Reservation.objects.all()  # Fetch all reservations
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservations:reservation_success')
    else:
        # Pre-fill the form with the user's data
        initial_data = {
            'full_name': request.user.get_full_name(),
            'email': request.user.email,
            'phone': '',  # Optional
        }
        form = ReservationForm(initial=initial_data)
    
    return render(request, 'reservations/reserve_table.html', {'form': form})

def reservation_success(request):
    return render(request, 'reservations/reservation_success.html')
