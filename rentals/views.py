from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Rental
from .forms import RentalForm

def rental_list(request):
    contracts = Rental.objects.all()
    return render(request, 'rentals/rental_list.html', {'contracts': contracts})

def rental_create(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            car = form.cleaned_data['car']

            if Rental.objects.filter(car=car, active=True).exists():
                form.add_error('car', 'Este carro já está alugado.')
            else:
                form.save()
                redirect('rental_list')

    else:
        form = RentalForm()

    return render(request, 'rentals/rental_form.html', {'form': form})

def rental_finish(request, rental_id):
    contract = get_object_or_404(Rental, id=rental_id)

    contract.active = False
    contract.end_date = date.today()
    contract.save()

    return redirect('rental_list')
