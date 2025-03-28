from django.db import models
from accounts.models import CustomUser
from clients.models import Client

class WorkOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='work_orders')
    job_description = models.TextField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"WorkOrder #{self.id} for {self.client.name}"

    def update_status(self):
        # Skip if already completed
        if self.status == 'completed':
            return

        pickup = self.addresses.filter(address_type='pickup').first()
        dropoff = self.addresses.filter(address_type='dropoff').first()

        if pickup and pickup.scheduled_date and dropoff and dropoff.scheduled_date:
            self.status = 'in_progress'
        else:
            self.status = 'pending'

    def save(self, *args, **kwargs):
        self.update_status()
        super().save(*args, **kwargs)

class WorkOrderAddress(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('pickup', 'Pickup'),
        ('dropoff', 'Dropoff'),
    ]
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='addresses')
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)
    address = models.CharField(max_length=255)
    scheduled_date = models.DateField(blank=True, null=True)  # ✅ Field used for scheduling

    def __str__(self):
        return f"{self.get_address_type_display()} Address for WorkOrder #{self.work_order.id}"

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
