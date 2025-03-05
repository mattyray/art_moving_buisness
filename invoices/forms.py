from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoice_number',
            'client',
            'work_order',  # Optional: remove if you don't want to link invoices to work orders
            'due_date',
            'amount',
            'status',
            'notes',
        ]
