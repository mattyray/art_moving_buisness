# workorders/views/pdf_views.py
"""
PDF generation views for work orders
"""

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from weasyprint import HTML

from ..models import WorkOrder
from ..queries import WorkOrderQueries


@login_required
def workorder_pdf(request, pk):
    """Generate PDF for work order with optimized queries"""
    # Use optimized query to get work order with all related data
    workorder = get_object_or_404(
        WorkOrderQueries.get_optimized_base(), 
        pk=pk
    )
    
    # Related data is already prefetched
    events = workorder.events.all().order_by('date')
    notes = workorder.notes.all().order_by('-created_at')
    attachments = workorder.attachments.exclude(file__exact='')
    
    html_string = render_to_string("workorders/workorder_pdf.html", {
        "job": workorder,
        "events": events,
        "notes": notes,
        "attachments": attachments,
    })
    
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f"inline; filename=WorkOrder_{workorder.id}.pdf"
    return response