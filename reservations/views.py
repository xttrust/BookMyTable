from django.shortcuts import render, get_object_or_404, redirect
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
            return redirect('reservation_success')  # Redirect to a success page or list view
    else:
        form = ReservationForm()
    
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_success(request):
    return render(request, 'reservations/reservation_success.html')
