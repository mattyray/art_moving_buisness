from django import forms
from .models import WorkOrder, JobAttachment, JobNote

class WorkOrderForm(forms.ModelForm):
    scheduled_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',  # This class will trigger Flatpickr
                'placeholder': 'YYYY-MM-DD'
            }
        )
    )
    
    class Meta:
        model = WorkOrder
        fields = [
            'client',
            'pickup_address',
            'dropoff_address',
            'job_description',
            'estimated_cost',
            'assigned_to',
            'status',
            'scheduled_date',
        ]

class JobAttachmentForm(forms.ModelForm):
    class Meta:
        model = JobAttachment
        fields = ['file']

class JobNoteForm(forms.ModelForm):
    class Meta:
        model = JobNote
        fields = ['note']
