from django.contrib import admin
from .models import Client

from import_export.admin import ImportExportModelAdmin
from .resources import ClientResource

@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource
    list_display = ('id', 'name', 'email', 'phone', 'address')



