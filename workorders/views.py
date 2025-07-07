from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import WorkOrder, Event, JobAttachment, JobNote
from .forms import WorkOrderForm, EventFormSet, JobAttachmentForm, JobNoteForm

# workorders/views.py
from django.template.loader import render_to_string
from weasyprint import HTML

def workorder_pdf(request, pk):
    workorder = get_object_or_404(WorkOrder, pk=pk)
    html_string = render_to_string("workorders/workorder_pdf.html", {
        "job": workorder,
        "events": workorder.events.all().order_by('date'),
        "notes": workorder.notes.all().order_by('-created_at'),
        "attachments": workorder.attachments.exclude(file__exact=''),
    })
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    # Changed from attachment to inline so it opens in browser for printing
    response["Content-Disposition"] = f"inline; filename=WorkOrder_{workorder.id}.pdf"
    return response


@login_required
def workorder_calendar_data(request):
    """Returns only pending and scheduled events for calendar display, excluding completed jobs."""
    events = []

    # A simple palette to pick a distinct color per work order:
    palette = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
    ]
    def get_color(wo_id):
        return palette[wo_id % len(palette)]

    # Only scheduled Event objects for pending and in-progress jobs (no completed jobs)
    scheduled_events = Event.objects.filter(
        date__isnull=False,
        work_order__status__in=["pending", "in_progress"]
    )
    for evt in scheduled_events:
        events.append({
            "title": f"{evt.get_event_type_display()}: {evt.work_order.client.name}",
            "start": evt.date.isoformat(),
            "color": get_color(evt.work_order.id),
            "url": f"/workorders/detail/{evt.work_order.id}/",
        })

    return JsonResponse(events, safe=False)


@login_required
def workorder_list(request):
    query = request.GET.get('q', '')

    pending_jobs = WorkOrder.objects.exclude(events__date__isnull=False)\
                                    .filter(status__in=["pending", "in_progress"])
    scheduled_jobs = WorkOrder.objects.filter(
        events__date__isnull=False,
        status__in=["pending", "in_progress"]
    ).distinct()

    completed_invoiced_jobs = WorkOrder.objects.filter(status='completed', invoiced=True)
    completed_uninvoiced_jobs = WorkOrder.objects.filter(status='completed', invoiced=False)

    if query:
        pending_jobs = pending_jobs.filter(client__name__icontains=query)
        scheduled_jobs = scheduled_jobs.filter(client__name__icontains=query)
        completed_invoiced_jobs = completed_invoiced_jobs.filter(client__name__icontains=query)
        completed_uninvoiced_jobs = completed_uninvoiced_jobs.filter(client__name__icontains=query)

    context = {
        'query': query,
        'pending_jobs': pending_jobs.order_by('-updated_at')[:5],
        'scheduled_jobs': scheduled_jobs.order_by('-updated_at')[:5],
        'completed_invoiced_jobs': completed_invoiced_jobs.order_by('-completed_at')[:5],
        'completed_uninvoiced_jobs': completed_uninvoiced_jobs.order_by('-completed_at')[:5],
    }
    return render(request, 'workorders/workorder_list.html', context)


@login_required
def workorder_create(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        event_formset = EventFormSet(request.POST, prefix="events")
        attachment_form = JobAttachmentForm(request.POST, request.FILES)
        note_form = JobNoteForm(request.POST)

        if form.is_valid() and event_formset.is_valid():
            workorder = form.save()
            event_formset.instance = workorder
            event_formset.save()

            workorder.update_status()
            workorder.save()

            if attachment_form.is_valid():
                uploaded = request.FILES.get('file')
                if uploaded:
                    attachment = attachment_form.save(commit=False)
                    attachment.work_order = workorder
                    attachment.save()

            if note_form.is_valid():
                text = note_form.cleaned_data.get('note', '').strip()
                if text:
                    note = note_form.save(commit=False)
                    note.work_order = workorder
                    note.save()

            # Handle different submit buttons
            if 'save_and_invoice' in request.POST:
                messages.success(request, f"Work order #{workorder.id} created successfully.")
                return redirect(f'/invoices/create/?work_order={workorder.id}')
            elif 'save_and_complete' in request.POST:
                workorder.status = 'completed'
                workorder.completed_at = timezone.now()
                workorder.save()
                messages.success(request, f"Work order #{workorder.id} created and marked as completed.")
                return redirect("workorder_detail", job_id=workorder.id)
            else:  # save_only
                messages.success(request, f"Work order #{workorder.id} created successfully.")
                return redirect("workorder_detail", job_id=workorder.id)
    else:
        form = WorkOrderForm()
        event_formset = EventFormSet(prefix="events")
        attachment_form = JobAttachmentForm()
        note_form = JobNoteForm()

    return render(request, 'workorders/workorder_form.html', {
        'form': form,
        'event_formset': event_formset,
        'attachment_form': attachment_form,
        'note_form': note_form,
    })


@login_required
def workorder_edit(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if request.method == 'POST':
        form = WorkOrderForm(request.POST, instance=workorder)
        event_formset = EventFormSet(request.POST, instance=workorder, prefix="events")
        attachment_form = JobAttachmentForm(request.POST, request.FILES)
        note_form = JobNoteForm(request.POST)

        if form.is_valid() and event_formset.is_valid():
            form.save()
            event_formset.save()

            workorder.update_status()
            workorder.save()

            if attachment_form.is_valid():
                uploaded = request.FILES.get('file')
                if uploaded:
                    attachment = attachment_form.save(commit=False)
                    attachment.work_order = workorder
                    attachment.save()

            if note_form.is_valid():
                text = note_form.cleaned_data.get('note', '').strip()
                if text:
                    note = note_form.save(commit=False)
                    note.work_order = workorder
                    note.save()

            # Handle different submit buttons
            if 'save_and_invoice' in request.POST:
                messages.success(request, f"Work order #{workorder.id} updated successfully.")
                return redirect(f'/invoices/create/?work_order={workorder.id}')
            elif 'save_and_complete' in request.POST:
                workorder.status = 'completed'
                workorder.completed_at = timezone.now()
                workorder.save()
                messages.success(request, f"Work order #{workorder.id} updated and marked as completed.")
                return redirect("workorder_detail", job_id=workorder.id)
            else:  # save_only
                messages.success(request, f"Work order #{workorder.id} updated successfully.")
                return redirect("workorder_detail", job_id=workorder.id)
    else:
        form = WorkOrderForm(instance=workorder)
        event_formset = EventFormSet(instance=workorder, prefix="events")
        attachment_form = JobAttachmentForm()
        note_form = JobNoteForm()

    return render(request, "workorders/workorder_form.html", {
        'form': form,
        'event_formset': event_formset,
        'attachment_form': attachment_form,
        'note_form': note_form,
        'job': workorder,
    })


@login_required
def workorder_delete(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if request.method == 'POST':
        workorder.delete()
        messages.success(request, "Work order deleted successfully.")
        return redirect('workorder_list')
    return render(request, 'workorders/workorder_confirm_delete.html', {'workorder': workorder})


@login_required
def mark_scheduled(request, job_id):
    return redirect('workorder_edit', job_id=job_id)


@login_required
def mark_completed(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if workorder.status in ['pending', 'in_progress']:
        workorder.status = 'completed'
        workorder.completed_at = timezone.now()
        workorder.save()
        messages.success(request, "Work order marked as completed.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('workorder_list')))


@login_required
def complete_and_invoice(request, job_id):
    """Mark work order as completed and redirect to invoice creation"""
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if workorder.status in ['pending', 'in_progress']:
        workorder.status = 'completed'
        workorder.completed_at = timezone.now()
        workorder.save()
        messages.success(request, f"Work order #{job_id} marked as completed.")
    
    return redirect(f'/invoices/create/?work_order={workorder.id}')


@login_required
def mark_paid(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)

    if workorder.status == 'completed' and not workorder.invoiced:
        workorder.invoiced = True
        workorder.save()
        messages.success(request, f"Work order #{job_id} marked as paid.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('completed_jobs')))


@login_required
def mark_completed_and_paid(request, job_id):
    """Mark work order as completed and paid in one action"""
    workorder = get_object_or_404(WorkOrder, id=job_id)
    
    if workorder.status in ['pending', 'in_progress']:
        workorder.status = 'completed'
        workorder.completed_at = timezone.now()
    
    workorder.invoiced = True
    workorder.save()
    messages.success(request, f"Work order #{job_id} marked as completed and paid.")
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('workorder_list')))


@login_required
def workorder_detail(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    events = workorder.events.all()
    attachments = workorder.attachments.exclude(file__exact='')
    notes = workorder.notes.all()

    attachment_form = JobAttachmentForm()
    note_form = JobNoteForm()

    if request.method == 'POST':
        if 'attachment_submit' in request.POST:
            attachment_form = JobAttachmentForm(request.POST, request.FILES)
            uploaded = request.FILES.get('file')
            if attachment_form.is_valid() and uploaded:
                attachment = attachment_form.save(commit=False)
                attachment.work_order = workorder
                attachment.save()
            return redirect('workorder_detail', job_id=workorder.id)

        elif 'note_submit' in request.POST:
            note_form = JobNoteForm(request.POST)
            if note_form.is_valid():
                text = note_form.cleaned_data.get('note', '').strip()
                if text:
                    note = note_form.save(commit=False)
                    note.work_order = workorder
                    note.save()
            return redirect('workorder_detail', job_id=workorder.id)

    return render(request, 'workorders/workorder_detail.html', {
        'job': workorder,
        'events': events,
        'attachments': attachments,
        'notes': notes,
        'attachment_form': attachment_form,
        'note_form': note_form,
    })


@login_required
def pending_jobs_view(request):
    query = request.GET.get('q', '')
    jobs = WorkOrder.objects.exclude(events__date__isnull=False)\
                            .filter(status__in=["pending", "in_progress"])\
                            .order_by('-updated_at')
    if query:
        jobs = jobs.filter(client__name__icontains=query)
    return render(request, 'workorders/pending_jobs.html', {'jobs': jobs, 'query': query})


@login_required
def scheduled_jobs_view(request):
    query = request.GET.get('q', '')
    jobs = WorkOrder.objects.filter(events__date__isnull=False,
                                    status__in=["pending", "in_progress"])\
                            .distinct()\
                            .order_by('-updated_at')
    if query:
        jobs = jobs.filter(client__name__icontains=query)
    return render(request, 'workorders/scheduled_jobs.html', {'jobs': jobs, 'query': query})


@login_required
def completed_jobs_view(request):
    query = request.GET.get('q', '')

    uninvoiced_jobs = WorkOrder.objects.filter(status='completed', invoiced=False).order_by('-completed_at')
    invoiced_jobs = WorkOrder.objects.filter(status='completed', invoiced=True).order_by('-completed_at')

    if query:
        uninvoiced_jobs = uninvoiced_jobs.filter(client__name__icontains=query)
        invoiced_jobs = invoiced_jobs.filter(client__name__icontains=query)

    context = {
        'query': query,
        'uninvoiced_jobs': uninvoiced_jobs,
        'invoiced_jobs': invoiced_jobs,
    }
    return render(request, 'workorders/completed_jobs.html', context)

@login_required
def change_workorder_status(request, job_id):
    """Change work order status with confirmation"""
    workorder = get_object_or_404(WorkOrder, id=job_id)
    new_status = request.POST.get('new_status')
    
    if request.method == 'POST' and new_status in ['pending', 'in_progress', 'completed']:
        old_status = workorder.status
        workorder.status = new_status
        
        # Handle completion timestamp
        if new_status == 'completed' and not workorder.completed_at:
            workorder.completed_at = timezone.now()
        elif new_status != 'completed':
            workorder.completed_at = None
            
        workorder.save()
        
        # Create a status change message
        status_messages = {
            'pending': 'moved back to Pending',
            'in_progress': 'marked as In Progress', 
            'completed': 'marked as Completed'
        }
        
        messages.success(request, f"Work Order #{job_id} {status_messages[new_status]}.")
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('workorder_list')))

@login_required
def reset_workorder_invoiced(request, job_id):
    """Reset the invoiced flag on a work order"""
    workorder = get_object_or_404(WorkOrder, id=job_id)
    
    if request.method == 'POST':
        workorder.invoiced = False
        workorder.save()
        messages.success(request, f"Work Order #{job_id} invoiced status reset.")
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('workorder_list')))

@login_required
def load_more_workorders(request):
    """AJAX endpoint to load more work orders"""
    if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    section = request.GET.get('section')
    offset = int(request.GET.get('offset', 0))
    limit = 5
    
    # Determine which queryset to use based on section
    if section == 'pending':
        jobs = WorkOrder.objects.exclude(events__date__isnull=False)\
                                .filter(status__in=["pending", "in_progress"])\
                                .order_by('-updated_at')[offset:offset+limit]
    elif section == 'scheduled':
        jobs = WorkOrder.objects.filter(
            events__date__isnull=False,
            status__in=["pending", "in_progress"]
        ).distinct().order_by('-updated_at')[offset:offset+limit]
    elif section == 'completed':
        jobs = WorkOrder.objects.filter(
            status='completed', 
            invoiced=False
        ).order_by('-completed_at')[offset:offset+limit]
    elif section == 'invoiced':
        jobs = WorkOrder.objects.filter(
            status='completed', 
            invoiced=True
        ).order_by('-completed_at')[offset:offset+limit]
    else:
        return JsonResponse({'error': 'Invalid section'}, status=400)
    
    # Check if there are more items after this batch
    has_more = len(jobs) == limit
    if has_more:
        # Check if there are actually more items beyond this batch
        if section == 'pending':
            total_count = WorkOrder.objects.exclude(events__date__isnull=False)\
                                          .filter(status__in=["pending", "in_progress"]).count()
        elif section == 'scheduled':
            total_count = WorkOrder.objects.filter(
                events__date__isnull=False,
                status__in=["pending", "in_progress"]
            ).distinct().count()
        elif section == 'completed':
            total_count = WorkOrder.objects.filter(status='completed', invoiced=False).count()
        elif section == 'invoiced':
            total_count = WorkOrder.objects.filter(status='completed', invoiced=True).count()
        
        has_more = (offset + limit) < total_count
    
    # Render the jobs using the partial template
    from django.template.loader import render_to_string
    html = render_to_string('workorders/partials/job_rows.html', {
        'jobs': jobs,
        'section': section,
    }, request=request)
    
    return JsonResponse({
        'html': html,
        'count': len(jobs),
        'has_more': has_more,
    })