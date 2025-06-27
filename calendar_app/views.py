from django.shortcuts import render
from datetime import datetime, timedelta, date
from workorders.models import Event
from django.db.models import Q


def parse_mmddyy(date_str):
    return datetime.strptime(date_str, '%m-%d-%y').date()

def week_detail(request, date):
    # parse and compute week start/end
    day   = parse_mmddyy(date)
    start = day - timedelta(days=day.weekday())
    end   = start + timedelta(days=6)

    # build a simple list of each date in that week
    week_days = [start + timedelta(days=i) for i in range(7)]

    # fetch events in the range
    events = Event.objects.filter(date__range=(start, end))

    # optional filtering
    q = request.GET.get('q', '')
    if q:
        events = events.filter(
            Q(work_order__client__name__icontains=q) |
            Q(event_type__icontains=q)
        )

    context = {
        'start': start,
        'end': end,
        'week_days': week_days,
        'events': events,
        'query': q,
    }
    return render(request, 'calendar/week_detail.html', context)


def day_detail(request, date):
    # date is mm-dd-yy
    day = parse_mmddyy(date)

    events = Event.objects.filter(date=day)

    q = request.GET.get('q', '')
    if q:
        events = events.filter(
            Q(work_order__client__name__icontains=q) |
            Q(event_type__icontains=q)
        )

    context = {
        'day': day,
        'events': events,
        'query': q,
    }
    return render(request, 'calendar/day_detail.html', context)