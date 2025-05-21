from django import forms
from .models import Invoice
from workorders.models import WorkOrder

class InvoiceForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'YYYY-MM-DD'
        })
    )

    class Meta:
        model = Invoice
        fields = [
            'work_order',
            'due_date',
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
