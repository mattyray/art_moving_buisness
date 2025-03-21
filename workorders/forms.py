from django import forms
from django.forms import inlineformset_factory
from .models import WorkOrder, WorkOrderAddress, JobAttachment, JobNote

class WorkOrderForm(forms.ModelForm):
    scheduled_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',  # Triggers Flatpickr
                'placeholder': 'YYYY-MM-DD'
            }
        ),
        required=False
    )
    
    class Meta:
        model = WorkOrder
        # Removed 'status' so it auto-updates based on scheduled_date
        fields = [
            'client',
            'job_description',
            'estimated_cost',
            'assigned_to',
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
    extra=4,
    can_delete=True
)


class JobAttachmentForm(forms.ModelForm):
    file = forms.FileField(required=False)  # Make file upload optional

    class Meta:
        model = JobAttachment
        fields = ['file']


class JobNoteForm(forms.ModelForm):
    class Meta:
        model = JobNote
        fields = ['note']
