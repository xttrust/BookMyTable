from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm
from table.models import Table
from datetime import datetime, time


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
        reservation_time = request.POST.get('reservation_time', '').strip()
        number_of_people = request.POST.get('number_of_people', '').strip()
        table_id = request.POST.get('table', '').strip()

        # Perform additional validation for required fields
        if not full_name:
            messages.error(request, 'Full Name is required.')
        elif not email:
            messages.error(request, 'Email is required.')
        elif not reservation_date:
            messages.error(request, 'Reservation Date is required.')
        elif not reservation_time:
            messages.error(request, 'Reservation Time is required.')
        elif not number_of_people or not number_of_people.isdigit() or int(number_of_people) <= 0:
            messages.error(request, 'Number of People must be a positive integer.')
        elif not table_id:
            messages.error(request, 'Table selection is required.')
        else:
            # Additional time validation
            reservation_time = datetime.strptime(reservation_time, '%H:%M').time()
            start_time = time(8, 0)  # 8 AM
            end_time = time(21, 0)  # 9 PM

            if not (start_time <= reservation_time <= end_time):
                messages.error(request, f"Reservation time must be between {start_time.strftime('%H:%M')} and {end_time.strftime('%H:%M')}.")
            elif form.is_valid():
                # Check for existing reservations that conflict with the new reservation
                reservation_datetime = datetime.combine(
                    form.cleaned_data['reservation_date'], 
                    form.cleaned_data['reservation_time']
                )
                conflicting_reservations = Reservation.objects.filter(
                    table_id=table_id,
                    reservation_date=form.cleaned_data['reservation_date'],
                    reservation_time=form.cleaned_data['reservation_time']
                )
                if conflicting_reservations.exists():
                    messages.error(request, 'The selected table is already booked for this time.')
                else:
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