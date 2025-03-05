from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Invoice
from .forms import InvoiceForm
from clients.models import Client
from workorders.models import WorkOrder
from django.db.models import Q

def invoice_list(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.all().order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) |
            Q(client__name__icontains=query)
        )
    context = {'invoices': invoices, 'query': query}
    return render(request, 'invoices/invoice_list.html', context)

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    context = {'invoice': invoice}
    return render(request, 'invoices/invoice_detail.html', context)

def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    context = {'form': form}
    return render(request, 'invoices/invoice_form.html', context)

def invoice_update(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm(instance=invoice)
    context = {'form': form, 'invoice': invoice}
    return render(request, 'invoices/invoice_form.html', context)

# Optional: AJAX view to get work orders for a selected client
def get_workorders_for_client(request):
    client_id = request.GET.get('client_id')
    work_orders = WorkOrder.objects.filter(client_id=client_id).values('id', 'job_description', 'estimated_cost')
    return JsonResponse(list(work_orders), safe=False)
