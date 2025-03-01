from django.shortcuts import render, redirect
from .models import WorkOrder
from .forms import WorkOrderForm

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
    # Pending: No scheduled date and status is still pending
    pending_jobs = WorkOrder.objects.filter(status='pending', scheduled_date__isnull=True)
    # Scheduled: Has a scheduled date and status is pending or in progress
    scheduled_jobs = WorkOrder.objects.filter(status__in=['pending', 'in_progress'], scheduled_date__isnull=False)
    # Completed: Status is completed
    completed_jobs = WorkOrder.objects.filter(status='completed')
    
    return render(request, 'workorders/jobs_overview.html', {
         'pending_jobs': pending_jobs,
         'scheduled_jobs': scheduled_jobs,
         'completed_jobs': completed_jobs,
    })
