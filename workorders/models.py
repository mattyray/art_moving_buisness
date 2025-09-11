from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image
import os
import uuid
from io import BytesIO
import cloudinary
from cloudinary.models import CloudinaryField

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
    
    # NEW: Event completion tracking fields
    completed = models.BooleanField(default=False, help_text='Mark if this specific event was completed')
    completed_at = models.DateTimeField(blank=True, null=True, help_text='When this event was marked complete')
    completed_by = models.CharField(max_length=100, blank=True, help_text='Who marked this event complete')

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
        print(f"🔧 JobAttachment.save() called for file: {self.file.name if self.file else 'No file'}")
        
        if self.file:
            # Ensure file has content and is not empty
            if not hasattr(self.file, 'size') or self.file.size == 0:
                print(f"❌ File is empty or has no size")
                raise ValidationError("Empty file cannot be uploaded")
                
            print(f"✅ File size: {self.file.size} bytes")
            self.file_size = self.file.size
            
            # Set file type based on extension
            ext = os.path.splitext(self.file.name)[1].lower()
            print(f"📄 File extension: {ext}")
            
            if ext in ['.jpg', '.jpeg', '.png', '.gif']:
                self.file_type = 'image'
            elif ext == '.pdf':
                self.file_type = 'pdf'
            elif ext in ['.doc', '.docx']:
                self.file_type = 'document'
            else:
                self.file_type = 'text'
            
            print(f"🏷️ File type set to: {self.file_type}")
            
            # Create thumbnail for images AFTER saving the main file
            if self.file_type == 'image' and not self.thumbnail:
                try:
                    print(f"🖼️ Will create thumbnail after saving main file")
                    # Store that we need to create thumbnail, but do it after save
                    self._create_thumbnail_after_save = True
                except Exception as e:
                    print(f"⚠️ Warning: Could not prepare thumbnail: {e}")
        
        print(f"💾 Saving JobAttachment to database")
        super().save(*args, **kwargs)
        
        # Create thumbnail AFTER the main file is saved
        if hasattr(self, '_create_thumbnail_after_save') and self._create_thumbnail_after_save:
            try:
                print(f"🖼️ Creating thumbnail after main file save")
                self.create_thumbnail()
                # Remove the flag
                del self._create_thumbnail_after_save
            except Exception as e:
                print(f"⚠️ Warning: Could not create thumbnail after save: {e}")
        
        print(f"✅ JobAttachment saved successfully with ID: {self.id}")
    def create_thumbnail(self):
        if not self.file:
            return
        
        try:
            # Reset file pointer to beginning
            self.file.seek(0)
            image = Image.open(self.file)
            image.thumbnail((200, 200), Image.Resampling.LANCZOS)
            
            thumb_name = f"thumb_{uuid.uuid4().hex}.jpg"
            thumb_io = BytesIO()
            image.save(thumb_io, 'JPEG', quality=85)
            thumb_io.seek(0)
            
            from django.core.files.base import ContentFile
            self.thumbnail.save(thumb_name, ContentFile(thumb_io.read()), save=False)
            print(f"✅ Thumbnail created successfully: {thumb_name}")
        except Exception as e:
            print(f"❌ Error creating thumbnail: {e}")
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

    def file_exists(self):
        """Check if the file actually exists"""
        try:
            return self.file and self.file.storage.exists(self.file.name)
        except:
            return False

    def get_file_url(self):
        """Get the correct URL for file type - images vs raw files"""
        try:
            if self.file and hasattr(self.file, 'public_id') and self.file.public_id:
                # For Cloudinary files, build the correct URL based on file type
                if self.file_type == 'image':
                    # Images use /image/upload/ path
                    return cloudinary.CloudinaryImage(self.file.public_id).build_url()
                else:
                    # Documents, PDFs, text files use /raw/upload/ path
                    return cloudinary.CloudinaryImage(self.file.public_id).build_url(
                        resource_type="raw"
                    )
            elif self.file and hasattr(self.file, 'url'):
                # Fallback to regular file URL (for local storage)
                return self.file.url
        except Exception as e:
            print(f"Error getting file URL: {e}")
        return None

    def get_thumbnail_url(self):
        """Get optimized thumbnail URL - only for images"""
        if self.file_type == 'image':
            try:
                # First try Cloudinary transformation if available
                if hasattr(self.file, 'public_id') and self.file.public_id:
                    return cloudinary.CloudinaryImage(self.file.public_id).build_url(
                        width=200, height=200, crop="fill", quality="auto", fetch_format="auto"
                    )
                # Fall back to local thumbnail
                elif self.thumbnail and hasattr(self.thumbnail, 'url'):
                    return self.thumbnail.url
                # Fall back to original image
                elif self.file and hasattr(self.file, 'url'):
                    return self.file.url
            except Exception as e:
                print(f"Error getting thumbnail URL: {e}")
        return None

    def get_display_url(self):
        """Get optimized display URL - same as file URL for documents"""
        if self.file_type == 'image':
            try:
                if hasattr(self.file, 'public_id') and self.file.public_id:
                    # Cloudinary - return optimized display image
                    return cloudinary.CloudinaryImage(self.file.public_id).build_url(
                        width=800, height=600, crop="limit", quality="auto", fetch_format="auto"
                    )
            except:
                pass
        # For documents/PDFs/text, just return the regular file URL
        return self.get_file_url()


class JobNote(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.id} for WorkOrder {self.work_order.id}"