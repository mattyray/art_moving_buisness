from django.db import models
from django.conf import settings

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

    def __str__(self):
        return f"{self.get_event_type_display()} for WorkOrder #{self.work_order.id}"


class JobAttachment(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='job_attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment {self.id} for WorkOrder {self.work_order.id}"


class JobNote(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.id} for WorkOrder {self.work_order.id}"
