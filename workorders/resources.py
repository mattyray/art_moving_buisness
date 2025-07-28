from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, DateWidget
from .models import WorkOrder, Event, JobAttachment
from clients.models import Client

# --------------------------
# ✅ WorkOrder Resource (Enhanced)
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
# ✅ Event Resource (Enhanced)
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
        fields = ('id', 'work_order', 'event_type', 'address', 'date', 'daily_order', 'scheduled_time')
        skip_unchanged = True
        report_skipped = True

    def before_import_row(self, row, **kwargs):
        """Clean and validate data before import"""
        # Handle null/empty dates
        if not row.get('date') or row.get('date') == '':
            row['date'] = None
            
        # Validate event_type
        valid_types = ['pickup', 'pickup_wrap', 'wrap', 'install', 'deliver_install', 'dropoff']
        if row.get('event_type') not in valid_types:
            raise ValueError(f"Invalid event_type: {row.get('event_type')}")
            
        return super().before_import_row(row, **kwargs)

    def skip_row(self, instance, original, row, import_validation_errors=None):
        """Skip rows with missing work_order or invalid data"""
        # Skip if work_order doesn't exist
        work_order_id = row.get('work_order_id')
        if work_order_id:
            try:
                WorkOrder.objects.get(id=work_order_id)
            except WorkOrder.DoesNotExist:
                print(f"Skipping Event {row.get('id')} - WorkOrder {work_order_id} does not exist")
                return True
        
        return False

# --------------------------
# ✅ JobAttachment Resource (NEW)
# --------------------------
class JobAttachmentResource(resources.ModelResource):
    work_order = fields.Field(
        column_name='work_order_id',
        attribute='work_order',
        widget=ForeignKeyWidget(WorkOrder, 'id')
    )
    uploaded_at = fields.Field(
        column_name='uploaded_at',
        attribute='uploaded_at',
        widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S')
    )
    file_size_mb = fields.Field(
        column_name='file_size_mb',
        attribute='file_size'
    )

    class Meta:
        model = JobAttachment
        import_id_fields = ['id']
        fields = (
            'id',
            'work_order',
            'file',
            'file_type',
            'file_size_mb',
            'uploaded_at',
        )
        skip_unchanged = True
        report_skipped = True

    def dehydrate_file_size_mb(self, attachment):
        """Convert file size to MB for export"""
        if attachment.file_size:
            return round(attachment.file_size / (1024 * 1024), 2)
        return None

    def before_import_row(self, row, **kwargs):
        """Clean and validate data before import"""
        # Validate file_type
        valid_types = ['image', 'pdf', 'document', 'text']
        if row.get('file_type') and row.get('file_type') not in valid_types:
            raise ValueError(f"Invalid file_type: {row.get('file_type')}")
            
        return super().before_import_row(row, **kwargs)

    def skip_row(self, instance, original, row, import_validation_errors=None):
        """Skip rows with missing work_order or file"""
        # Skip if work_order doesn't exist
        work_order_id = row.get('work_order_id')
        if work_order_id:
            try:
                WorkOrder.objects.get(id=work_order_id)
            except WorkOrder.DoesNotExist:
                print(f"Skipping JobAttachment {row.get('id')} - WorkOrder {work_order_id} does not exist")
                return True
        
        # Skip if no file
        if not row.get('file'):
            print(f"Skipping JobAttachment {row.get('id')} - No file specified")
            return True
        
        return False