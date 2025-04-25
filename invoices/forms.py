from django import forms
from .models import Invoice
from clients.models import Client
from workorders.models import WorkOrder

class InvoiceForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control select2',
            'style': 'width: 100%;',
            'placeholder': 'Search for a client...',
        })
    )
    work_order = forms.ModelChoiceField(
        queryset=WorkOrder.objects.none(),  # Start empty; will be populated via AJAX
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control select2',
            'style': 'width: 100%;',
            'placeholder': 'Select a work order...',
            'disabled': 'disabled',          # Disabled until a client is chosen
        })
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'YYYY-MM-DD'
        })
    )
    
    class Meta:
        model = Invoice
        fields = [
            'client',
            'work_order',
            'due_date',
            'amount',
            'status',
            'notes',
        ]
