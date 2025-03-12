from django import forms
from django.forms import inlineformset_factory
from .models import WorkOrder, WorkOrderAddress, JobAttachment, JobNote

class WorkOrderForm(forms.ModelForm):
    scheduled_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',  # This will trigger Flatpickr
                'placeholder': 'YYYY-MM-DD'
            }
        ),
        required=False
    )
    
    class Meta:
        model = WorkOrder
        fields = [
            'client',
            'job_description',
            'estimated_cost',
            'assigned_to',
            'status',
            'scheduled_date',
        ]

class WorkOrderAddressForm(forms.ModelForm):
    class Meta:
        model = WorkOrderAddress
        fields = ['address_type', 'address']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

WorkOrderAddressFormSet = inlineformset_factory(
    WorkOrder, WorkOrderAddress,
    form=WorkOrderAddressForm,
    extra=1,  # Adjust as needed
    can_delete=True
)

class JobAttachmentForm(forms.ModelForm):
    class Meta:
        model = JobAttachment
        fields = ['file']

class JobNoteForm(forms.ModelForm):
    class Meta:
        model = JobNote
        fields = ['note']
