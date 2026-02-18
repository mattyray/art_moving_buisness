import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from workorders.models import Event
import json


def get_event_color(work_order_id):
    """Generate consistent colors for work orders"""
    palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
               "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
    return palette[work_order_id % len(palette)]


@login_required
def week_detail(request, week_str):
    # Parse week_str (format: mm-dd-yy for the Monday of that week)
    month, day, year = week_str.split('-')
    if len(year) == 2:
        year = '20' + year
    
    start = datetime.date(int(year), int(month), int(day))
    
    # Calculate the Monday of this week if not already Monday
    days_since_monday = start.weekday()
    start = start - datetime.timedelta(days=days_since_monday)
    
    query = request.GET.get('q', '')
    
    # Get events for the week
    end = start + datetime.timedelta(days=6)
    events = Event.objects.filter(
        date__gte=start,
        date__lte=end
    ).select_related('work_order__client').order_by('date', 'daily_order', 'scheduled_time', 'id')
    
    if query:
        events = events.filter(work_order__client__name__icontains=query)
    
    # Add colors to events
    events_with_colors = []
    for event in events:
        event.color = get_event_color(event.work_order.id)
        events_with_colors.append(event)
    
    context = {
        'start': start,
        'events': events_with_colors,
        'query': query,
    }
    return render(request, 'calendar/week_detail.html', context)


@login_required
def day_detail(request, day_str):
    # Parse day_str (format: mm-dd-yy)
    month, day, year = day_str.split('-')
    if len(year) == 2:
        year = '20' + year
    
    day = datetime.date(int(year), int(month), int(day))
    query = request.GET.get('q', '')
    
    # Get events for this day, ordered by daily_order, then time, then id
    events = Event.objects.filter(date=day).select_related('work_order__client').order_by('daily_order', 'scheduled_time', 'id')
    
    if query:
        events = events.filter(work_order__client__name__icontains=query)
    
    # Add colors and order numbers to events
    events_with_data = []
    for i, event in enumerate(events, 1):
        event.color = get_event_color(event.work_order.id)
        event.display_order = i
        events_with_data.append(event)
    
    context = {
        'day': day,
        'events': events_with_data,
        'query': query,
    }
    return render(request, 'calendar/day_detail.html', context)


@login_required
@require_http_methods(["POST"])
def update_daily_order(request, day_str):
    """AJAX endpoint to save daily event ordering and times"""
    try:
        # Parse the date
        month, day, year = day_str.split('-')
        if len(year) == 2:
            year = '20' + year
        day_date = datetime.date(int(year), int(month), int(day))
        
        data = json.loads(request.body)
        event_updates = data.get('events', [])
        
        # Update each event
        for update in event_updates:
            event_id = update.get('id')
            daily_order = update.get('order')
            scheduled_time = update.get('time')
            
            # Handle the time field more safely
            if scheduled_time:
                scheduled_time = str(scheduled_time).strip()
                if not scheduled_time:  # If it's an empty string after stripping
                    scheduled_time = None
            else:
                scheduled_time = None
            
            event = Event.objects.get(id=event_id, date=day_date)
            event.daily_order = daily_order
            event.scheduled_time = scheduled_time
            event.save(update_fields=['daily_order', 'scheduled_time'])
        
        return JsonResponse({'success': True})
        
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)