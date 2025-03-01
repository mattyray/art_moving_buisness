from django import forms
from .models import WorkOrder

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'client',
            'pickup_address',
            'dropoff_address',
            'email',
            'phone',
            'home_address',
            'job_description',
            'estimated_cost',
            'assigned_to',
            'status',
            'scheduled_date',  # Use scheduled_date instead of deadline if desired
        ]
