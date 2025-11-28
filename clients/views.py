from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'clients/client_detail.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    return render(request, 'clients/client_create.html', {'form': form})
