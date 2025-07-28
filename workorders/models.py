from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image
import os
import uuid

def validate_file_type(file):
    allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.gif', '.doc', '.docx', '.txt']
    file_extension = os.path.splitext(file.name)[1].lower()
    if file_extension not in allowed_extensions:
        raise ValidationError(f'File type not allowed. Allowed: {", ".join(allowed_extensions)}')

def validate_file_size(file):
    max_size = 10 * 1024 * 1024  # 10MB
    if file.size > max_size:
        raise ValidationError(f'File too large. Max size: 10MB.')

def job_attachment_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    return f'job_attachments/{unique_filename}'

class WorkOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='work_orders'
    )
    job_description = models.TextField(blank=True, null=True)
    estimated_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoiced = models.BooleanField(default=False)

    def __str__(self):
        return f"WorkOrder #{self.id} for {self.client.name}"

    def update_status(self):
        if self.status == 'completed':
            return
        if self.events.filter(date__isnull=False).exists():
            self.status = 'in_progress'
        else:
            self.status = 'pending'


class Event(models.Model):
    EVENT_TYPES = [
        ('pickup', 'Pickup'),
        ('pickup_wrap', 'Pickup and Wrap'),
        ('wrap', 'Wrap'),
        ('install', 'Install'),
        ('deliver_install', 'Deliver and Install'),
        ('dropoff', 'Drop Off'),
    ]
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=30, choices=EVENT_TYPES)
    address = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True, null=True)
    daily_order = models.PositiveIntegerField(blank=True, null=True, help_text='Order of this event within the day')
    scheduled_time = models.TimeField(blank=True, null=True, help_text='Scheduled time for this event')

    class Meta:
        ordering = ['date', 'daily_order', 'scheduled_time', 'id']

    def __str__(self):
        return f"{self.get_event_type_display()} for WorkOrder #{self.work_order.id}"


class JobAttachment(models.Model):
    FILE_TYPE_CHOICES = [
        ('image', 'Image'),
        ('pdf', 'PDF'),
        ('document', 'Document'),
        ('text', 'Text'),
    ]
    
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(
        upload_to=job_attachment_upload_path,
        validators=[validate_file_type, validate_file_size]
    )
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES, blank=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='job_attachments/thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment {self.id} for WorkOrder {self.work_order.id}"
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
            
            # Set file type based on extension
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.gif']:
                self.file_type = 'image'
            elif ext == '.pdf':
                self.file_type = 'pdf'
            elif ext in ['.doc', '.docx']:
                self.file_type = 'document'
            else:
                self.file_type = 'text'
            
            # Create thumbnail for images
            if self.file_type == 'image' and not self.thumbnail:
                self.create_thumbnail()
        
        super().save(*args, **kwargs)
    
    def create_thumbnail(self):
        if not self.file:
            return
        
        try:
            image = Image.open(self.file)
            image.thumbnail((200, 200), Image.Resampling.LANCZOS)
            
            thumb_name = f"thumb_{uuid.uuid4().hex}.jpg"
            thumb_io = BytesIO()
            image.save(thumb_io, 'JPEG', quality=85)
            thumb_io.seek(0)
            
            from django.core.files.base import ContentFile
            self.thumbnail.save(thumb_name, ContentFile(thumb_io.read()), save=False)
        except Exception:
            pass  # Skip thumbnail creation if it fails

    def get_file_icon(self):
        """Return Bootstrap icon class for file type"""
        icons = {
            'image': 'bi-image',
            'pdf': 'bi-file-earmark-pdf',
            'document': 'bi-file-earmark-word',
            'text': 'bi-file-earmark-text',
        }
        return icons.get(self.file_type, 'bi-file-earmark')


class JobNote(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.id} for WorkOrder {self.work_order.id}"