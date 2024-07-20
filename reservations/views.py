from django.contrib import messages
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
        
        # Extract values from POST request
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        reservation_date = request.POST.get('reservation_date', '').strip()
        number_of_people = request.POST.get('number_of_people', '').strip()

        # Perform additional validation for required fields
        if not full_name:
            messages.error(request, 'Full Name is required.')
        elif not email:
            messages.error(request, 'Email is required.')
        elif not reservation_date:
            messages.error(request, 'Reservation Date is required.')
        elif not number_of_people or not number_of_people.isdigit() or int(number_of_people) <= 0:
            messages.error(request, 'Number of People must be a positive integer.')
        elif form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservations:reservation_success')
        else:
            # If form is not valid, get errors and show them
            for field, errors in form.errors.as_data().items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')

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
