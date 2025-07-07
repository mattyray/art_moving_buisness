# workorders/views/crud_views.py
"""
Create, Read, Update, Delete views for work orders
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from ..models import WorkOrder
from ..forms import WorkOrderForm, EventFormSet, JobAttachmentForm, JobNoteForm
from ..queries import WorkOrderQueries


@login_required
def workorder_create(request):
    """Create new work order with optimized form handling"""
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

            # Handle attachment
            if attachment_form.is_valid():
                uploaded = request.FILES.get('file')
                if uploaded:
                    attachment = attachment_form.save(commit=False)
                    attachment.work_order = workorder
                    attachment.save()

            # Handle note
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
    """Edit work order with optimized queries"""
    # Use optimized query to get work order with related data
    workorder = get_object_or_404(
        WorkOrderQueries.get_optimized_base(), 
        id=job_id
    )
    
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

            # Handle attachment
            if attachment_form.is_valid():
                uploaded = request.FILES.get('file')
                if uploaded:
                    attachment = attachment_form.save(commit=False)
                    attachment.work_order = workorder
                    attachment.save()

            # Handle note
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
def workorder_detail(request, job_id):
    """Work order detail view with optimized queries"""
    # Use optimized query to get work order with all related data
    workorder = get_object_or_404(
        WorkOrderQueries.get_optimized_base(),
        id=job_id
    )
    
    # Related data is already prefetched, no additional queries needed
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
def workorder_delete(request, job_id):
    """Delete work order"""
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if request.method == 'POST':
        workorder.delete()
        messages.success(request, "Work order deleted successfully.")
        return redirect('workorder_list')
    return render(request, 'workorders/workorder_confirm_delete.html', {'workorder': workorder})