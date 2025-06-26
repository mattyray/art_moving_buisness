# invoices/resources.py
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import Invoice
from clients.models import Client
from workorders.models import WorkOrder

class InvoiceResource(resources.ModelResource):
    client = fields.Field(
        column_name='client_id',
        attribute='client',
        widget=ForeignKeyWidget(Client, 'id')
    )
    work_order = fields.Field(
        column_name='work_order_id',
        attribute='work_order',
        widget=ForeignKeyWidget(WorkOrder, 'id')
    )
    date_created = fields.Field(
        column_name='date_created',
        attribute='date_created',
        widget=DateWidget(format='%Y-%m-%d')
    )

    class Meta:
        model = Invoice
        import_id_fields = ['id']
        fields = (
            'id',
            'client',
            'work_order',
            'invoice_number',
            'date_created',
            'amount',
            'status',
            'notes',
        )
        skip_unchanged = True
        report_skipped = True