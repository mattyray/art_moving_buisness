from import_export import resources
from .models import Client

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        import_id_fields = ['id']
        fields = ('id', 'name', 'email', 'phone', 'address')
        skip_unchanged = True
        report_skipped = True

    def skip_row(self, instance, original, row, import_validation_errors=None):
        return not instance.name
