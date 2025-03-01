from django import forms
from .models import WorkOrder, JobAttachment, JobNote

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
