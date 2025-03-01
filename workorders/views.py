from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import WorkOrder, JobAttachment, JobNote
from .forms import WorkOrderForm, JobAttachmentForm, JobNoteForm

def workorder_list(request):
    orders = WorkOrder.objects.all().order_by('-created_at')
    return render(request, 'workorders/workorder_list.html', {'orders': orders})

def workorder_create(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workorder_list')
    else:
        form = WorkOrderForm()
    return render(request, 'workorders/workorder_form.html', {'form': form})

def jobs_overview(request):
    query = request.GET.get('q', '')
    
    # Pending: no scheduled date and status is pending
    pending_jobs = WorkOrder.objects.filter(status='pending', scheduled_date__isnull=True)
    # Scheduled: has a scheduled date and status pending or in progress
    scheduled_jobs = WorkOrder.objects.filter(status__in=['pending', 'in_progress'], scheduled_date__isnull=False)
    # Completed: status is completed
    completed_jobs = WorkOrder.objects.filter(status='completed')
    
    if query:
        pending_jobs = pending_jobs.filter(client__name__icontains=query)
        scheduled_jobs = scheduled_jobs.filter(client__name__icontains=query)
        completed_jobs = completed_jobs.filter(client__name__icontains=query)
    
    context = {
        'pending_jobs': pending_jobs,
        'scheduled_jobs': scheduled_jobs,
        'completed_jobs': completed_jobs,
        'query': query,
    }
    return render(request, 'workorders/jobs_overview.html', context)

def mark_scheduled(request, job_id):
    job = get_object_or_404(WorkOrder, id=job_id)
    if job.status == 'pending':
        job.status = 'in_progress'
        if not job.scheduled_date:
            job.scheduled_date = timezone.now().date()
        job.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('jobs_overview')))

def mark_completed(request, job_id):
    job = get_object_or_404(WorkOrder, id=job_id)
    if job.status in ['pending', 'in_progress']:
        job.status = 'completed'
        job.completed_at = timezone.now()
        job.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('jobs_overview')))

def workorder_detail(request, job_id):
    job = get_object_or_404(WorkOrder, id=job_id)
    attachments = job.attachments.all()
    notes = job.notes.all()

    if request.method == 'POST':
        if 'attachment_submit' in request.POST:
            attachment_form = JobAttachmentForm(request.POST, request.FILES)
            if attachment_form.is_valid():
                attachment = attachment_form.save(commit=False)
                attachment.work_order = job
                attachment.save()
                return redirect('workorder_detail', job_id=job.id)
        elif 'note_submit' in request.POST:
            note_form = JobNoteForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.work_order = job
                note.save()
                return redirect('workorder_detail', job_id=job.id)
    else:
        attachment_form = JobAttachmentForm()
        note_form = JobNoteForm()

    context = {
        'job': job,
        'attachments': attachments,
        'notes': notes,
        'attachment_form': attachment_form,
        'note_form': note_form,
    }
    return render(request, 'workorders/workorder_detail.html', context)
