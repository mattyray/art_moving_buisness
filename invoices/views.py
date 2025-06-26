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
def invoice_delete(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == "POST":
        invoice.delete()
        messages.success(request, "Invoice deleted successfully.")
        return redirect('invoice_list')
    return render(request, 'invoices/invoice_confirm_delete.html', {'invoice': invoice})

@login_required
def invoice_list(request):
    query = request.GET.get('q', '')
    unpaid_invoices = Invoice.objects.filter(status='unpaid')
    in_quickbooks_invoices = Invoice.objects.filter(status='in_quickbooks')
    paid_invoices = Invoice.objects.filter(status='paid')
    
    if query:
        unpaid_invoices = unpaid_invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
        in_quickbooks_invoices = in_quickbooks_invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
        paid_invoices = paid_invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    
    unpaid_invoices = unpaid_invoices.order_by('-date_created')[:5]
    in_quickbooks_invoices = in_quickbooks_invoices.order_by('-date_created')[:5]
    paid_invoices = paid_invoices.order_by('-date_created')[:5]
    
    context = {
        'query': query,
        'unpaid_invoices': unpaid_invoices,
        'paid_invoices': in_quickbooks_invoices,  # Template expects 'paid_invoices' for middle section
        'overdue_invoices': paid_invoices,  # Template expects 'overdue_invoices' for final section
    }
    return render(request, 'invoices/invoice_list.html', context)

@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    # grab events if there's a linked work order
    events = []
    if invoice.work_order:
        events = invoice.work_order.events.all().order_by('date')

    return render(request, 'invoices/invoice_detail.html', {
        'invoice': invoice,
        'events': events,
    })

@login_required
def invoice_update(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    # Always show the invoice's existing events
    events = []
    if invoice.work_order:
        events = invoice.work_order.events.all()

    # Instantiate form with instance
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
    else:
        form = InvoiceForm(instance=invoice)

    # Filter work_order to that invoice's client
    if invoice.client:
        form.fields['work_order'].queryset = WorkOrder.objects.filter(
            client=invoice.client,
            status='completed'
        )

    # Handle save
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('invoice_detail', invoice_id=invoice.id)

    return render(request, 'invoices/invoice_form.html', {
        'form': form,
        'events': events,
        'invoice': invoice,
    })

@login_required
def mark_invoice_paid(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    
    if invoice.status == 'unpaid':
        invoice.status = 'in_quickbooks'
        invoice.save()
        messages.warning(request, "Invoice marked as In QuickBooks.")
    elif invoice.status == 'in_quickbooks':
        invoice.status = 'paid'
        invoice.save()
        messages.success(request, "Invoice marked as Paid.")
    
    return redirect('invoice_list')

@login_required
def get_workorders_for_client(request):
    client_id = request.GET.get('client_id')
    work_orders = WorkOrder.objects.filter(client_id=client_id).values('id', 'job_description', 'estimated_cost')
    return JsonResponse(list(work_orders), safe=False)

# ✅ RENAMED: invoice_unpaid (already had correct name)
@login_required
def invoice_unpaid(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.filter(status='unpaid').order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    return render(request, 'invoices/invoice_unpaid.html', {'invoices': invoices, 'query': query})

# ✅ RENAMED: invoice_paid -> invoice_in_quickbooks (shows 'in_quickbooks' status)
@login_required
def invoice_in_quickbooks(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.filter(status='in_quickbooks').order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    return render(request, 'invoices/invoice_in_quickbooks.html', {'invoices': invoices, 'query': query})

# ✅ RENAMED: invoice_overdue -> invoice_paid (shows 'paid' status)
@login_required
def invoice_paid(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.filter(status='paid').order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    return render(request, 'invoices/invoice_paid.html', {'invoices': invoices, 'query': query})

@login_required
def invoice_create(request):
    work_order_id = request.GET.get('work_order')
    work_order = None
    events = []

    if work_order_id:
        try:
            work_order = WorkOrder.objects.get(id=work_order_id)
            events = work_order.events.all()
        except WorkOrder.DoesNotExist:
            messages.error(request, "Invalid work order.")
            return redirect('invoice_list')

    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.status = 'unpaid'
            invoice.date_created = timezone.now()

            if work_order:
                invoice.client = work_order.client
                invoice.work_order = work_order
                work_order.invoiced = True
                work_order.save()

            invoice.save()
            messages.success(request, "Invoice created successfully.")
            return redirect('invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm(initial={'work_order': work_order})

    form.fields['work_order'].queryset = WorkOrder.objects.filter(status='completed')

    return render(request, 'invoices/invoice_form.html', {
        'form': form,
        'client_id': work_order.client.id if work_order else None,
        'events': events,
    })

# ---------- AJAX VIEWS ----------

@login_required
def ajax_get_clients(request):
    """Return JSON list of clients matching the query term."""
    q = request.GET.get('q', '')
    clients = Client.objects.filter(name__icontains=q).order_by('name')[:20]
    results = [{'id': c.id, 'text': c.name} for c in clients]
    return JsonResponse(results, safe=False)

@login_required
def ajax_get_active_workorders(request):
    """Return JSON list of completed work orders for a given client."""
    client_id = request.GET.get('client_id')
    if not client_id:
        return JsonResponse([], safe=False)
    
    work_orders = WorkOrder.objects.filter(
        client_id=client_id,
        status='completed'
    )

    results = [
        {
            'id': wo.id,
            'text': f"Order #{wo.id} – {wo.job_description[:40]}{'...' if len(wo.job_description) > 40 else ''}"
        }
        for wo in work_orders
    ]
    return JsonResponse(results, safe=False)