from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, DateWidget
from .models import WorkOrder, Event
from clients.models import Client

# --------------------------
# ✅ WorkOrder Resource
# --------------------------
class WorkOrderResource(resources.ModelResource):
    client = fields.Field(
        column_name='client_id',
        attribute='client',
        widget=ForeignKeyWidget(Client, 'id')  # Looks up Client by ID
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
            'client',
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


# --------------------------
# ✅ Event Resource
# --------------------------
class EventResource(resources.ModelResource):
    work_order = fields.Field(
        column_name='work_order_id',
        attribute='work_order',
        widget=ForeignKeyWidget(WorkOrder, 'id')
    )
    date = fields.Field(
        column_name='date',
        attribute='date',
        widget=DateWidget(format='%Y-%m-%d')
    )

    class Meta:
        model = Event
        import_id_fields = ['id']
        fields = ('id', 'work_order', 'event_type', 'address', 'date')
        skip_unchanged = True
        report_skipped = True
