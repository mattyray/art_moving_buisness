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
def invoice_calendar_data(request):
    """Fetch invoices for the calendar (unpaid, overdue, paid)."""
    invoices = Invoice.objects.all()
    events = []

    for invoice in invoices:
        if invoice.status == "unpaid":
            events.append({
                "title": f"Unpaid Invoice: {invoice.client.name}",
                "start": invoice.due_date.isoformat(),
                "color": "red",
                "url": f"/invoices/{invoice.id}/",
            })
        elif invoice.status == "overdue":
            events.append({
                "title": f"Overdue Invoice: {invoice.client.name}",
                "start": invoice.due_date.isoformat(),
                "color": "darkred",
                "url": f"/invoices/{invoice.id}/",
            })
        elif invoice.status == "paid":
            events.append({
                "title": f"Paid Invoice: {invoice.client.name}",
                "start": invoice.due_date.isoformat(),
                "color": "green",
                "url": f"/invoices/{invoice.id}/",
            })
    return JsonResponse(events, safe=False)

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

    # grab events if there’s a linked work order
    events = []
    if invoice.work_order:
        events = invoice.work_order.events.all().order_by('date')

    return render(request, 'invoices/invoice_detail.html', {
        'invoice': invoice,
        'events': events,
    })


@login_required
def invoice_create(request):
    client_id = request.GET.get('client') or request.POST.get('client')
    work_order_id = request.GET.get('work_order') or request.POST.get('work_order')

    events = []
    initial_data = {}

    if work_order_id:
        wo = get_object_or_404(WorkOrder, id=work_order_id)
        client_id = wo.client.id
        events = wo.events.all()
        initial_data['client'] = client_id
        initial_data['work_order'] = work_order_id
    elif client_id:
        initial_data['client'] = client_id

    if request.method == 'POST':
        form = InvoiceForm(request.POST)

        # 1) filter work_order choices before validation
        if client_id:
            form.fields['work_order'].queryset = WorkOrder.objects.filter(
                client_id=client_id,
                status='completed'
            )
        else:
            form.fields['work_order'].queryset = WorkOrder.objects.none()

        # 2) set default status so validation won’t fail
        form.fields['status'].initial = 'unpaid'

        if form.is_valid():
            invoice = form.save(commit=False)
            # 3) manually bind the client FK from your hidden field
            cid = request.POST.get('client')
            if cid:
                invoice.client = get_object_or_404(Client, id=cid)
            invoice.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(initial={**initial_data, 'status':'unpaid'})
        # also preload work_orders on GET
        if client_id:
            form.fields['work_order'].queryset = WorkOrder.objects.filter(
                client_id=client_id,
                status='completed'
            )
        else:
            form.fields['work_order'].queryset = WorkOrder.objects.none()

    return render(request, 'invoices/invoice_form.html', {
        'form': form,
        'events': events,
        'invoice': None,
        'client_id': client_id,   # for your hidden input
    })


@login_required
def invoice_update(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    # Always show the invoice’s existing events
    events = invoice.work_order.events.all()

    # Instantiate form with instance
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
    else:
        form = InvoiceForm(instance=invoice)

    # Filter work_order to that invoice’s client
    form.fields['work_order'].queryset = WorkOrder.objects.filter(
        client=invoice.client,
        status__in=['pending', 'scheduled']
    )

    # Handle save
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('invoice_detail', invoice_id=invoice.id)

    return render(request, 'invoices/invoice_form.html', {
        'form': form,
        'events': events,
        'invoice': invoice,  # so template knows this is “edit” mode
    })


@login_required
def mark_invoice_paid(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.status = 'paid'
    invoice.save()
    messages.success(request, "Invoice marked as paid.")
    return redirect('invoice_list')

@login_required
def update_due_date(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == 'POST':
        new_due_date = request.POST.get('new_due_date')
        if new_due_date:
            invoice.due_date = new_due_date
            invoice.status = 'paid'
            invoice.save()
            messages.success(request, "Invoice due date updated and marked as paid.")
            return redirect('invoice_list')
        else:
            messages.error(request, "Please select a valid date.")
    return render(request, 'invoices/update_due_date.html', {'invoice': invoice})

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
    return render(request, 'invoices/invoice_unpaid.html', {'invoices': invoices, 'query': query})

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
def invoice_overdue(request):
    query = request.GET.get('q', '')
    invoices = Invoice.objects.filter(status='overdue').order_by('-date_created')
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) | Q(client__name__icontains=query)
        )
    return render(request, 'invoices/invoice_overdue.html', {'invoices': invoices, 'query': query})

# ---------- NEW AJAX VIEWS BELOW ----------
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
    """
    Return JSON list of active work orders for a given client.
    Only 'pending' and 'scheduled' statuses are considered active.
    """
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
