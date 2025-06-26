from django import forms
from .models import Invoice
from workorders.models import WorkOrder

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'work_order',
            'amount',
            'status',
            'notes',
        ]
        widgets = {
            'work_order': forms.Select(attrs={'class': 'form-control select2'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }