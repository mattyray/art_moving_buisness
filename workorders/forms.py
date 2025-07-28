from django import forms
from django.forms import inlineformset_factory
from django.apps import apps
from .models import WorkOrder, Event, JobAttachment, JobNote

class WorkOrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=None,
        widget=forms.Select(attrs={
            'class': 'form-control select2',
            'data-placeholder': 'Search or select a client'
        }),
        label="Client"
    )

    class Meta:
        model = WorkOrder
        fields = [
            'client',
            'job_description',
            'estimated_cost',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Client = apps.get_model('clients', 'Client')
        self.fields['client'].queryset = Client.objects.all()

        self.fields['job_description'].required = False
        self.fields['estimated_cost'].required = False
        self.fields['estimated_cost'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '0.00'
        })

class EventForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'YYYY-MM-DD'
        })
    )
    event_type = forms.ChoiceField(
        required=False,
        choices=[('', '---------')] + Event.EVENT_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Event Type"
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Address"
    )

    class Meta:
        model = Event
        fields = ['event_type', 'address', 'date']

EventFormSet = inlineformset_factory(
    WorkOrder,
    Event,
    form=EventForm,
    extra=1,
    can_delete=True
)

class JobAttachmentForm(forms.ModelForm):
    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.jpg,.jpeg,.png,.gif,.doc,.docx,.txt'
        }),
        help_text='Allowed: PDF, Images (JPG/PNG/GIF), Word docs, Text files. Max 10MB.'
    )

    class Meta:
        model = JobAttachment
        fields = ['file']

class JobNoteForm(forms.ModelForm):
    note = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 
        label="Note"
    )

    class Meta:
        model = JobNote
        fields = ['note']