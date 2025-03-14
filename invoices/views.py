from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Invoice
from .forms import InvoiceForm
from clients.models import Client
from workorders.models import WorkOrder
from django.utils import timezone

@login_required
def invoice_list(request):
    query = request.GET.get('q', '')
    unpaid_invoices = Invoice.objects.filter(status='unpaid')
    paid_invoices = Invoice.objects.filter(status='paid')
    overdue_invoices = Invoice.objects.filter(status='overdue')
    
    if query:
        unpaid_invoices = unpaid_invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
        paid_invoices = paid_invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
        overdue_invoices = overdue_invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    
    unpaid_invoices = unpaid_invoices.order_by('-date_created')[:3]
    paid_invoices = paid_invoices.order_by('-date_created')[:3]
    overdue_invoices = overdue_invoices.order_by('-date_created')[:3]
    
    context = {
        'query': query,
        'unpaid_invoices': unpaid_invoices,
        'paid_invoices': paid_invoices,
        'overdue_invoices': overdue_invoices,
    }
    return render(request, 'invoices/invoice_list.html', context)

@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    context = {'invoice': invoice}
    return render(request, 'invoices/invoice_detail.html', context)

@login_required
def invoice_create(request):
    work_order_id = request.GET.get('work_order')
    pickup_addresses = None
    dropoff_addresses = None
    initial_data = {}

    if work_order_id:
        work_order = get_object_or_404(WorkOrder, id=work_order_id)
        pickup_addresses = work_order.addresses.filter(address_type='pickup')
        dropoff_addresses = work_order.addresses.filter(address_type='dropoff')
        initial_data = {
            'client': work_order.client.id,
            'work_order': work_order.id,
            'amount': work_order.estimated_cost,
        }

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(initial=initial_data)

    context = {
        'form': form,
        'pickup_addresses': pickup_addresses,
        'dropoff_addresses': dropoff_addresses,
    }
    return render(request, 'invoices/invoice_form.html', context)

@login_required
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

# New view to mark an invoice as paid (for unpaid invoices)
@login_required
def mark_invoice_paid(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.status = 'paid'
    invoice.save()
    messages.success(request, "Invoice marked as paid.")
    return redirect('invoice_list')

# N@login_required
def update_due_date(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == 'POST':
        new_due_date = request.POST.get('new_due_date')
        if new_due_date:
            invoice.due_date = new_due_date
            # Optionally, mark as paid:
            invoice.status = 'paid'
            invoice.save()
            messages.success(request, "Invoice due date updated and marked as paid.")
            return redirect('invoice_list')
        else:
            messages.error(request, "Please select a valid date.")
    context = {'invoice': invoice}
    return render(request, 'invoices/update_due_date.html', context)

# AJAX view to get work orders for a selected client (unchanged)
@login_required
def get_workorders_for_client(request):
    client_id = request.GET.get('client_id')
    work_orders = WorkOrder.objects.filter(client_id=client_id).values('id', 'job_description', 'estimated_cost')
    return JsonResponse(list(work_orders), safe=False)

@login_required
def invoice_unpaid(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.filter(status='unpaid').order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    context = {'invoices': invoices, 'query': query}
    return render(request, 'invoices/invoice_unpaid.html', context)

@login_required
def invoice_paid(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.filter(status='paid').order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    context = {'invoices': invoices, 'query': query}
    return render(request, 'invoices/invoice_paid.html', context)

@login_required
def invoice_overdue(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.filter(status='overdue').order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    context = {'invoices': invoices, 'query': query}
    return render(request, 'invoices/invoice_overdue.html', context)
