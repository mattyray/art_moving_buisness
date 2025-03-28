from django import forms
from django.forms import inlineformset_factory
from clients.models import Client
from .models import WorkOrder, WorkOrderAddress, JobAttachment, JobNote

class WorkOrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control select2',
            'data-placeholder': 'Search or select a client'
        }),
        label="Client"
    )

    # Optional: remove this field if it's no longer needed globally
    scheduled_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',
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
            'scheduled_date',
        ]


class WorkOrderAddressForm(forms.ModelForm):
    scheduled_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'YYYY-MM-DD'
        })
    )

    class Meta:
        model = WorkOrderAddress
        fields = ['address_type', 'address', 'scheduled_date']
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
    file = forms.FileField(required=False)

    class Meta:
        model = JobAttachment
        fields = ['file']


class JobNoteForm(forms.ModelForm):
    note = forms.CharField(required=False, widget=forms.Textarea, label="Note")

    class Meta:
        model = JobNote
        fields = ['note']
