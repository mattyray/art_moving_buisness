from django.contrib import admin
from .models import WorkOrder, JobAttachment, JobNote

admin.site.register(WorkOrder)
admin.site.register(JobAttachment)
admin.site.register(JobNote)
