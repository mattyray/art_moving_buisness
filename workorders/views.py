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
    html_string = render_to_string("workorders/workorder_pdf.html", {"job": workorder})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f"filename=WorkOrder_{workorder.id}.pdf"
    return response



@login_required
def workorder_calendar_data(request):
    """Returns scheduled events for calendar display, color‐coding events by work order."""
    events = []

    # A simple palette to pick a distinct color per work order:
    palette = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
    ]
    def get_color(wo_id):
        return palette[wo_id % len(palette)]

    # Scheduled Event objects (only non‐completed jobs)
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

    # Pending jobs (no scheduled events yet)
    pending_jobs = WorkOrder.objects.exclude(events__date__isnull=False)\
                                    .filter(status__in=["pending", "in_progress"])
    for wo in pending_jobs:
        events.append({
            "title": f"Pending: {wo.client.name}",
            "start": wo.created_at.date().isoformat(),
            "color": "gray",
            "url": f"/workorders/detail/{wo.id}/",
        })

    # Completed jobs
    completed = WorkOrder.objects.filter(status='completed', completed_at__isnull=False)
    for wo in completed:
        events.append({
            "title": f"Completed: {wo.client.name}",
            "start": wo.completed_at.date().isoformat(),
            "color": "green",
            "url": f"/workorders/detail/{wo.id}/",
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
                attachment = attachment_form.save(commit=False)
                attachment.work_order = workorder
                attachment.save()

            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.work_order = workorder
                note.save()

            return redirect('workorder_list')
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
                attachment = attachment_form.save(commit=False)
                attachment.work_order = workorder
                attachment.save()

            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.work_order = workorder
                note.save()

            if 'create_invoice' in request.POST:
                return redirect(f'/invoices/create/?work_order={workorder.id}')
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
def workorder_detail(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    events      = workorder.events.all()
    # Exclude any attachment rows with no file path
    attachments = workorder.attachments.exclude(file__exact='')
    notes       = workorder.notes.all()

    attachment_form = JobAttachmentForm()
    note_form       = JobNoteForm()

    if request.method == 'POST':
        # --- New Attachment ---
        if 'attachment_submit' in request.POST:
            attachment_form = JobAttachmentForm(request.POST, request.FILES)
            # Only save when a file was uploaded
            uploaded = request.FILES.get('file')
            if attachment_form.is_valid() and uploaded:
                attachment = attachment_form.save(commit=False)
                attachment.work_order = workorder
                attachment.save()
            return redirect('workorder_detail', job_id=workorder.id)

        # --- New Note ---
        elif 'note_submit' in request.POST:
            note_form = JobNoteForm(request.POST)
            if note_form.is_valid():
                text = note_form.cleaned_data.get('note', '').strip()
                # Only save non‑empty notes
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
                            .order_by('-updated_at')  # ⬅️ Add this
    if query:
        jobs = jobs.filter(client__name__icontains=query)
    return render(request, 'workorders/pending_jobs.html', {'jobs': jobs, 'query': query})



@login_required
def scheduled_jobs_view(request):
    query = request.GET.get('q', '')
    jobs = WorkOrder.objects.filter(events__date__isnull=False,
                                    status__in=["pending", "in_progress"])\
                            .distinct()\
                            .order_by('-updated_at')  # ⬅️ Add this
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
