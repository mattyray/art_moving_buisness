from django.contrib import admin
from .models import WorkOrder, WorkOrderAddress, JobAttachment, JobNote

class WorkOrderAddressInline(admin.TabularInline):
    model = WorkOrderAddress
    extra = 1  # Number of extra empty forms

class WorkOrderAdmin(admin.ModelAdmin):
    inlines = [WorkOrderAddressInline]
    list_display = ['id', 'client', 'job_description', 'status']

admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(JobAttachment)
admin.site.register(JobNote)
