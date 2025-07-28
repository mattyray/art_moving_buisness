from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import WorkOrder, Event, JobAttachment, JobNote
from .resources import WorkOrderResource, EventResource

# --------------------------
# ✅ Inline for Events (for editing inside WorkOrder)
# --------------------------
class EventInline(admin.TabularInline):
    model = Event
    extra = 1

# --------------------------
# ✅ Inline for Attachments (for editing inside WorkOrder)
# --------------------------
class JobAttachmentInline(admin.TabularInline):
    model = JobAttachment
    extra = 0
    fields = ['file', 'file_type', 'file_size', 'thumbnail']
    readonly_fields = ['file_type', 'file_size', 'thumbnail']

# --------------------------
# ✅ Inline for Notes (for editing inside WorkOrder)
# --------------------------
class JobNoteInline(admin.TabularInline):
    model = JobNote
    extra = 0

# --------------------------
# ✅ WorkOrder Admin
# --------------------------
@admin.register(WorkOrder)
class WorkOrderAdmin(ImportExportModelAdmin):
    resource_class = WorkOrderResource
    inlines = [EventInline, JobAttachmentInline, JobNoteInline]
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
# ✅ Enhanced JobAttachment Admin
# --------------------------
@admin.register(JobAttachment)
class JobAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_order', 'file_name', 'file_type', 'file_size_display', 'uploaded_at']
    search_fields = ['file', 'work_order__id', 'work_order__client__name']
    list_filter = ['file_type', 'uploaded_at']
    readonly_fields = ['file_type', 'file_size', 'thumbnail', 'uploaded_at']
    
    def file_name(self, obj):
        return obj.file.name.split('/')[-1] if obj.file else 'No file'
    file_name.short_description = 'File Name'
    
    def file_size_display(self, obj):
        if obj.file_size:
            size_mb = obj.file_size / (1024 * 1024)
            if size_mb < 1:
                return f"{obj.file_size / 1024:.1f} KB"
            else:
                return f"{size_mb:.1f} MB"
        return 'Unknown'
    file_size_display.short_description = 'File Size'

# --------------------------
# ✅ JobNote Admin
# --------------------------
@admin.register(JobNote)
class JobNoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_order', 'note_preview', 'created_at']
    search_fields = ['note', 'work_order__id', 'work_order__client__name']
    list_filter = ['created_at']
    readonly_fields = ['created_at']
    
    def note_preview(self, obj):
        return obj.note[:50] + '...' if len(obj.note) > 50 else obj.note
    note_preview.short_description = 'Note Preview'