from django.shortcuts import render
from datetime import datetime, timedelta, date
from workorders.models import Event
from invoices.models import Invoice
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

    # fetch events/invoices in the range
    events   = Event.objects.filter(date__range=(start, end))
    invoices = Invoice.objects.filter(due_date__range=(start, end))

    # optional filtering
    q = request.GET.get('q', '')
    if q:
        events   = events.filter(
            Q(work_order__client__name__icontains=q) |
            Q(event_type__icontains=q)
        )
        invoices = invoices.filter(
            Q(client__name__icontains=q) |
            Q(invoice_number__icontains=q)
        )

    context = {
        'start': start,
        'end': end,
        'week_days': week_days,    # <-- pass this in
        'events': events,
        'invoices': invoices,
        'query': q,
    }
    return render(request, 'calendar/week_detail.html', context)

def month_detail(request):
    # Determine month/year from GET or default to today
    today = date.today()
    month = int(request.GET.get('month', today.month))
    year  = int(request.GET.get('year',  today.year))

    # Fetch all events & invoices in that month
    events   = Event.objects.filter(date__year=year, date__month=month)
    invoices = Invoice.objects.filter(due_date__year=year, due_date__month=month)

    # Optional search/filter param
    q = request.GET.get('q', '')
    if q:
        events   = events.filter(
            Q(work_order__client__name__icontains=q) |
            Q(event_type__icontains=q)
        )
        invoices = invoices.filter(
            Q(client__name__icontains=q) |
            Q(invoice_number__icontains=q)
        )

    context = {
        'year': year,
        'month': month,
        'events': events,
        'invoices': invoices,
        'query': q,
    }
    return render(request, 'calendar/month_detail.html', context)



def day_detail(request, date):
    # date is mm-dd-yy
    day = parse_mmddyy(date)

    events = Event.objects.filter(date=day)
    invoices = Invoice.objects.filter(due_date=day)

    q = request.GET.get('q', '')
    if q:
        events   = events.filter(
            Q(work_order__client__name__icontains=q) |
            Q(event_type__icontains=q)
        )
        invoices = invoices.filter(
            Q(client__name__icontains=q) |
            Q(invoice_number__icontains=q)
        )

    context = {
        'day': day,
        'events': events,
        'invoices': invoices,
        'query': q,
    }
    return render(request, 'calendar/day_detail.html', context)
