# workorders/views/ajax_views.py
"""
AJAX and API endpoint views for work orders
"""

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from ..models import Event
from ..queries import WorkOrderQueries


@login_required
def workorder_calendar_data(request):
    """Returns optimized calendar data for work order events"""
    events = []

    # Color palette for work orders
    palette = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
    ]
    
    def get_color(wo_id):
        return palette[wo_id % len(palette)]

    # Use optimized query for calendar events
    scheduled_events = WorkOrderQueries.get_calendar_events()
    
    for evt in scheduled_events:
        events.append({
            "title": f"{evt.get_event_type_display()}: {evt.work_order.client.name}",
            "start": evt.date.isoformat(),
            "color": get_color(evt.work_order.id),
            "url": f"/workorders/detail/{evt.work_order.id}/",
        })

    return JsonResponse(events, safe=False)


@login_required
def load_more_workorders(request):
    """Optimized AJAX endpoint to load more work orders"""
    if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    section = request.GET.get('section')
    offset = int(request.GET.get('offset', 0))
    limit = 5
    
    # Use optimized queries for load more
    if section == 'pending':
        jobs = list(WorkOrderQueries.get_pending_jobs()[offset:offset+limit])
        total_count = WorkOrderQueries.get_pending_jobs().count()
    elif section == 'scheduled':
        jobs = list(WorkOrderQueries.get_scheduled_jobs()[offset:offset+limit])
        total_count = WorkOrderQueries.get_scheduled_jobs().count()
    elif section == 'completed':
        jobs = list(WorkOrderQueries.get_completed_uninvoiced_jobs()[offset:offset+limit])
        total_count = WorkOrderQueries.get_completed_uninvoiced_jobs().count()
    elif section == 'invoiced':
        jobs = list(WorkOrderQueries.get_completed_invoiced_jobs()[offset:offset+limit])
        total_count = WorkOrderQueries.get_completed_invoiced_jobs().count()
    else:
        return JsonResponse({'error': 'Invalid section'}, status=400)
    
    # Check if there are more items after this batch
    has_more = (offset + limit) < total_count
    
    # Render templates
    context = {
        'jobs': jobs,
        'section': section,
    }
    
    desktop_html = render_to_string('workorders/partials/job_rows.html', context, request=request)
    mobile_html = render_to_string('workorders/partials/job_cards_mobile.html', context, request=request)
    
    return JsonResponse({
        'desktop_html': desktop_html,
        'mobile_html': mobile_html,
        'count': len(jobs),
        'has_more': has_more,
    })