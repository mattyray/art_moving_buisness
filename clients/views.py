from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm

@login_required
def client_list(request):
    query = request.GET.get('q', '')
    clients = Client.objects.all()
    if query:
        clients = clients.filter(name__icontains=query)
    context = {'clients': clients, 'query': query}
    return render(request, 'clients/client_list.html', context)

@login_required
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    # Work orders will be available through the reverse relationship: client.work_orders.all()
    context = {'client': client}
    return render(request, 'clients/client_detail.html', context)

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    context = {'form': form}
    return render(request, 'clients/client_form.html', context)

@login_required
def client_edit(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', client_id=client.id)
    else:
        form = ClientForm(instance=client)
    context = {'form': form, 'client': client}
    return render(request, 'clients/client_form.html', context)
