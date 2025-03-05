from django import forms
from .models import Invoice

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
            'client',
            'work_order',  # Optional: Remove if you don't need this link
            'due_date',
            'amount',
            'status',
            'notes',
        ]
