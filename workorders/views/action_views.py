# workorders/views/action_views.py
"""
Status change and action views for work orders
"""

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from ..models import WorkOrder


@login_required
def mark_completed(request, job_id):
    """Mark work order as completed"""
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
    """Mark work order as paid"""
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