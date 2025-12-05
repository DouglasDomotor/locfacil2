from django.shortcuts import render, get_object_or_404, redirect
from.models import Car
from .forms import CarForm 

def car_list(request):
    cars = Car.objects.all()
    return render(request, "car_list.html", {"cars": cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()

    return render(request, 'car_form.html', {'form': form})

def car_edit(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance = car)

    return render(request, 'car_form.html', {'form': form})

def car_delete(request, car_id):
    car =get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_comfirm_delete.html', {'car':car})
