from django.shortcuts import render, get_object_or_404, redirect
from.models import Car
from .forms import CarForm 

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()

    return render(request, 'cars/car_create.html', {'form': form})

def car_list(request):
    cars = Car.objects.all()
    return render(request, "car_list.html", {"cars": cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})
