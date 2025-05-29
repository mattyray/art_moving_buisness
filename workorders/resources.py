from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from .models import WorkOrder
from clients.models import Client



class WorkOrderResource(resources.ModelResource):
    client = fields.Field(
        column_name='client_id',
        attribute='client',
        widget=ForeignKeyWidget(Client, 'id')  # 👈 Tells it to lookup Client by ID
    )
    completed_at = fields.Field(
        column_name='completed_at',
        attribute='completed_at',
        widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S')
    )
    created_at = fields.Field(
        column_name='created_at',
        attribute='created_at',
        widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S')
    )
    updated_at = fields.Field(
        column_name='updated_at',
        attribute='updated_at',
        widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S')
    )

    class Meta:
        model = WorkOrder
        import_id_fields = ['id']
        fields = (
            'id',
            'client',  # 👈 Must match the attribute name
            'job_description',
            'estimated_cost',
            'status',
            'completed_at',
            'created_at',
            'updated_at',
            'invoiced',
        )
        skip_unchanged = True
        report_skipped = True

    def skip_row(self, instance, original, row, import_validation_errors=None):
        return not instance.job_description
