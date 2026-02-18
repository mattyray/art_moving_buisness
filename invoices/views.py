from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse  # ← This was missing
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.template.loader import render_to_string
from weasyprint import HTML

from .models import Invoice
from .forms import InvoiceForm
from clients.models import Client
from workorders.models import WorkOrder

# Add this function to invoices/views.py
@login_required 
def invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    
    # Get events if linked to work order
    events = []
    if invoice.work_order:
        events = invoice.work_order.events.all().order_by('date')
    
    html_string = render_to_string("invoices/invoice_pdf.html", {
        "invoice": invoice,
        "events": events,
    })
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    # Open in browser for printing
    response["Content-Disposition"] = f"inline; filename=Invoice_{invoice.invoice_number}.pdf"
    return response

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
        # ✅ Pre-populate form with work order data
        initial_data = {'work_order': work_order}
        if work_order and work_order.estimated_cost:
            initial_data['amount'] = work_order.estimated_cost
        
        form = InvoiceForm(initial=initial_data)

    form.fields['work_order'].queryset = WorkOrder.objects.filter(status='completed')

    return render(request, 'invoices/invoice_form.html', {
        'form': form,
        'client_id': work_order.client.id if work_order else None,
        'events': events,
        'work_order': work_order,  # ✅ Pass work order for template context
        'creating': True,  # ✅ Flag to show this is creation, not editing
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
            'text': f"Order #{wo.id} – {(wo.job_description or '')[:40]}{'...' if len(wo.job_description or '') > 40 else ''}"
        }
        for wo in work_orders
    ]
    return JsonResponse(results, safe=False)

@login_required
def change_invoice_status(request, invoice_id):
    """Change invoice status with confirmation"""
    invoice = get_object_or_404(Invoice, id=invoice_id)
    new_status = request.POST.get('new_status')
    
    if request.method == 'POST' and new_status in ['unpaid', 'in_quickbooks', 'paid']:
        old_status = invoice.status
        invoice.status = new_status
        invoice.save()
        
        # Create a status change message
        status_messages = {
            'unpaid': 'moved back to Not in QuickBooks',
            'in_quickbooks': 'marked as In QuickBooks',
            'paid': 'marked as Paid'
        }
        
        messages.success(request, f"Invoice #{invoice.invoice_number} {status_messages[new_status]}.")
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('invoice_list')))

@login_required
def load_more_invoices(request):
    """AJAX endpoint to load more invoices"""
    if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    section = request.GET.get('section')
    try:
        offset = int(request.GET.get('offset', 0))
    except (ValueError, TypeError):
        offset = 0
    limit = 5
    
    # Determine which queryset to use based on section
    if section == 'unpaid':
        invoices = Invoice.objects.filter(status='unpaid')\
                                 .order_by('-date_created')[offset:offset+limit]
    elif section == 'in_quickbooks':
        invoices = Invoice.objects.filter(status='in_quickbooks')\
                                 .order_by('-date_created')[offset:offset+limit]
    elif section == 'paid':
        invoices = Invoice.objects.filter(status='paid')\
                                 .order_by('-date_created')[offset:offset+limit]
    else:
        return JsonResponse({'error': 'Invalid section'}, status=400)
    
    # Check if there are more items after this batch
    has_more = len(invoices) == limit
    if has_more:
        # Check if there are actually more items beyond this batch
        if section == 'unpaid':
            total_count = Invoice.objects.filter(status='unpaid').count()
        elif section == 'in_quickbooks':
            total_count = Invoice.objects.filter(status='in_quickbooks').count()
        elif section == 'paid':
            total_count = Invoice.objects.filter(status='paid').count()
        
        has_more = (offset + limit) < total_count
    
    # Render separate templates for desktop and mobile
    from django.template.loader import render_to_string
    
    context = {
        'invoices': invoices,
        'section': section,
    }
    
    desktop_html = render_to_string('invoices/partials/invoice_rows.html', context, request=request)
    mobile_html = render_to_string('invoices/partials/invoice_cards_mobile.html', context, request=request)
    
    return JsonResponse({
        'desktop_html': desktop_html,
        'mobile_html': mobile_html,
        'count': len(invoices),
        'has_more': has_more,
    })