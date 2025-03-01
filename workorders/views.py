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
