from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WorkOrder, WorkOrderAddress, JobAttachment, JobNote
from .forms import WorkOrderForm, WorkOrderAddressFormSet, JobAttachmentForm, JobNoteForm

# Schedule a work order by setting a scheduled date and marking it as "in_progress"
@login_required
def schedule_workorder(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if request.method == "POST":
        scheduled_date = request.POST.get("scheduled_date")
        if scheduled_date:
            workorder.scheduled_date = scheduled_date
            # Update status to indicate scheduled; adjust as desired
            workorder.status = "in_progress"
            workorder.save()
            messages.success(request, "Work order scheduled successfully.")
        else:
            messages.error(request, "Please select a valid date.")
    return redirect('pending_jobs')

# Delete a work order
@login_required
def workorder_delete(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if request.method == 'POST':
        workorder.delete()
        messages.success(request, "Work order deleted successfully.")
        return redirect('workorder_list')
    context = {'workorder': workorder}
    return render(request, 'workorders/workorder_confirm_delete.html', context)

# List work orders with filtering for pending, scheduled, and completed
@login_required
def workorder_list(request):
    query = request.GET.get('q', '')
    pending_jobs = WorkOrder.objects.filter(status='pending', scheduled_date__isnull=True)
    scheduled_jobs = WorkOrder.objects.filter(status__in=['pending', 'in_progress'], scheduled_date__isnull=False)
    completed_jobs = WorkOrder.objects.filter(status='completed')

    if query:
        pending_jobs = pending_jobs.filter(client__name__icontains=query)
        scheduled_jobs = scheduled_jobs.filter(client__name__icontains=query)
        completed_jobs = completed_jobs.filter(client__name__icontains=query)

    context = {
        'query': query,
        'pending_jobs': pending_jobs.order_by('-updated_at')[:3],
        'scheduled_jobs': scheduled_jobs.order_by('-updated_at')[:3],
        'completed_jobs': completed_jobs.order_by('-updated_at')[:3],
    }
    return render(request, 'workorders/workorder_list.html', context)

# Create a new work order along with its addresses
@login_required
def workorder_create(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        address_formset = WorkOrderAddressFormSet(request.POST, prefix="addresses")
        if form.is_valid() and address_formset.is_valid():
            workorder = form.save()
            address_formset.instance = workorder
            address_formset.save()
            return redirect('workorder_list')
    else:
        form = WorkOrderForm()
        address_formset = WorkOrderAddressFormSet(prefix="addresses")
    context = {
        'form': form,
        'address_formset': address_formset,
    }
    return render(request, 'workorders/workorder_form.html', context)

# Edit an existing work order; supports two actions:
#   - Update only, redirecting to detail page.
#   - Update and create invoice, redirecting to invoice creation page with work_order data.
@login_required
def workorder_edit(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if request.method == 'POST':
        form = WorkOrderForm(request.POST, instance=workorder)
        address_formset = WorkOrderAddressFormSet(request.POST, instance=workorder, prefix="addresses")
        if form.is_valid() and address_formset.is_valid():
            form.save()
            address_formset.save()
            if 'create_invoice' in request.POST:
                return redirect('/invoices/create/?work_order=' + str(workorder.id))
            else:
                return redirect("workorder_detail", job_id=workorder.id)
    else:
        form = WorkOrderForm(instance=workorder)
        address_formset = WorkOrderAddressFormSet(instance=workorder, prefix="addresses")
    context = {
        'form': form,
        'address_formset': address_formset,
        'job': workorder,
    }
    return render(request, "workorders/workorder_form.html", context)

# Mark a pending work order as scheduled by setting its status and scheduled date (if not already set)
@login_required
def mark_scheduled(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if workorder.status == 'pending':
        workorder.status = 'in_progress'
        if not workorder.scheduled_date:
            workorder.scheduled_date = timezone.now().date()
        workorder.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('workorder_list')))

# Mark a work order as completed
@login_required
def mark_completed(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    if workorder.status in ['pending', 'in_progress']:
        workorder.status = 'completed'
        workorder.completed_at = timezone.now()
        workorder.save()
        messages.success(request, "Work order marked as completed.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('workorder_list')))

# Display the details for a single work order, along with attachments and notes
@login_required
def workorder_detail(request, job_id):
    workorder = get_object_or_404(WorkOrder, id=job_id)
    attachments = workorder.attachments.all()
    notes = workorder.notes.all()
    if request.method == 'POST':
        if 'attachment_submit' in request.POST:
            attachment_form = JobAttachmentForm(request.POST, request.FILES)
            if attachment_form.is_valid():
                attachment = attachment_form.save(commit=False)
                attachment.work_order = workorder
                attachment.save()
                return redirect('workorder_detail', job_id=workorder.id)
        elif 'note_submit' in request.POST:
            note_form = JobNoteForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.work_order = workorder
                note.save()
                return redirect('workorder_detail', job_id=workorder.id)
    else:
        attachment_form = JobAttachmentForm()
        note_form = JobNoteForm()
    context = {
        'job': workorder,
        'attachments': attachments,
        'notes': notes,
        'attachment_form': attachment_form,
        'note_form': note_form,
    }
    return render(request, 'workorders/workorder_detail.html', context)

# View for pending jobs
@login_required
def pending_jobs_view(request):
    query = request.GET.get('q', '')
    jobs = WorkOrder.objects.filter(status='pending', scheduled_date__isnull=True)
    if query:
        jobs = jobs.filter(client__name__icontains=query)
    context = {
        'jobs': jobs,
        'query': query,
    }
    return render(request, 'workorders/pending_jobs.html', context)

# View for scheduled jobs
@login_required
def scheduled_jobs_view(request):
    query = request.GET.get('q', '')
    jobs = WorkOrder.objects.filter(status__in=['pending', 'in_progress'], scheduled_date__isnull=False)
    if query:
        jobs = jobs.filter(client__name__icontains=query)
    context = {
        'jobs': jobs,
        'query': query,
    }
    return render(request, 'workorders/scheduled_jobs.html', context)

# View for completed jobs
@login_required
def completed_jobs_view(request):
    query = request.GET.get('q', '')
    jobs = WorkOrder.objects.filter(status='completed')
    if query:
        jobs = jobs.filter(client__name__icontains=query)
    context = {
        'jobs': jobs,
        'query': query,
    }
    return render(request, 'workorders/completed_jobs.html', context)
