from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import WorkOrder, Event, JobAttachment, JobNote
from .resources import WorkOrderResource, EventResource  # ✅ make sure both exist

# --------------------------
# ✅ Inline for Events (for editing inside WorkOrder)
# --------------------------
class EventInline(admin.TabularInline):
    model = Event
    extra = 1

# --------------------------
# ✅ WorkOrder Admin
# --------------------------
@admin.register(WorkOrder)
class WorkOrderAdmin(ImportExportModelAdmin):
    resource_class = WorkOrderResource
    inlines = [EventInline]
    list_display = ['id', 'client', 'job_description', 'status', 'invoiced', 'created_at', 'updated_at']
    search_fields = ['client__name', 'job_description']
    list_filter = ['status', 'invoiced', 'created_at', 'updated_at']

# --------------------------
# ✅ Event Admin (standalone import/export)
# --------------------------
@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource
    list_display = ['id', 'event_type', 'address', 'date', 'work_order']
    search_fields = ['event_type', 'address', 'work_order__job_description']
    list_filter = ['event_type', 'date']

# --------------------------
# ✅ Optional: JobAttachment/JobNote (basic admin)
# --------------------------
@admin.register(JobAttachment)
class JobAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_order', 'file', 'uploaded_at']
    readonly_fields = ['uploaded_at']

@admin.register(JobNote)
class JobNoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_order', 'note', 'created_at']
    readonly_fields = ['created_at']
