from django.contrib import admin
from .models import WorkOrder, Event, JobAttachment, JobNote

class EventInline(admin.TabularInline):
    model = Event
    extra = 1  # Number of extra empty forms

class WorkOrderAdmin(admin.ModelAdmin):
    inlines = [EventInline]
    list_display = ['id', 'client', 'job_description', 'status']
    search_fields = ['client__name', 'job_description']
    list_filter = ['status', 'created_at', 'updated_at']

admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(JobAttachment)
admin.site.register(JobNote)
