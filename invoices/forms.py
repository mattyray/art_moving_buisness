from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            # invoice_number is excluded since it auto-generates
            'client',
            'work_order',  # We will later make this dynamic
            'due_date',
            'amount',
            'status',
            'notes',
        ]
