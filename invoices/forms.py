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
        queryset=WorkOrder.objects.none(),  # default empty
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control select2',
            'style': 'width: 100%;',
            'placeholder': 'Select a work order...',
            'disabled': 'disabled',
        })
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'YYYY-MM-DD'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        client_id = None

        if 'client' in self.data:
            client_id = self.data.get('client')
        elif 'client' in self.initial:
            client_id = self.initial['client']
        elif self.instance and self.instance.pk:
            client_id = self.instance.client_id

        try:
            client_id = int(client_id)
            self.fields['work_order'].queryset = WorkOrder.objects.filter(
                client_id=client_id,
                status='completed'
            )
            self.fields['work_order'].widget.attrs.pop('disabled', None)
        except (TypeError, ValueError):
            self.fields['work_order'].queryset = WorkOrder.objects.none()


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
