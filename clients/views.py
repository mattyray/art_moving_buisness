from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
def client_create_ajax(request):
    """AJAX endpoint for creating clients from work order form"""
    if request.method == 'POST':
        try:
            # Create client from POST data
            client = Client(
                name=request.POST.get('name', '').strip(),
                email=request.POST.get('email', '').strip() or None,
                phone=request.POST.get('phone', '').strip() or None,
                address=request.POST.get('address', '').strip() or None,
                billing_address=request.POST.get('billing_address', '').strip() or None,
            )
            
            # Validate required fields
            if not client.name:
                return JsonResponse({'success': False, 'error': 'Name is required'})
            
            client.save()
            
            return JsonResponse({
                'success': True,
                'client': {
                    'id': client.id,
                    'name': client.name,
                    'email': client.email,
                    'phone': client.phone,
                    'address': client.address,
                    'billing_address': client.billing_address,
                }
            })
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

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