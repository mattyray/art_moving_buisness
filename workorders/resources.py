from import_export import resources
from .models import WorkOrder

class WorkOrderResource(resources.ModelResource):
    class Meta:
        model = WorkOrder
        import_id_fields = ['id']  # You can skip this if you're not importing with IDs
        fields = (
            'id',
            'client',          # This must match a valid Client ID
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
        return not instance.job_description  # Skip empty jobs
