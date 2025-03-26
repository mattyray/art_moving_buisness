from import_export import resources
from .models import Client

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        import_id_fields = []  # 👈 Don't rely on email or id for import uniqueness
        fields = ('name', 'email', 'phone', 'address')
        skip_unchanged = True
        report_skipped = True

    def skip_row(self, instance, original, row, import_validation_errors=None):
        # Skip row if name is completely missing
        return not instance.name
