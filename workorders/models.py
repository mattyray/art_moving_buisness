from django.db import models
from accounts.models import CustomUser

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class WorkOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='work_orders')
    pickup_address = models.CharField(max_length=255)
    dropoff_address = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    job_description = models.TextField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    scheduled_date = models.DateField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"WorkOrder #{self.id} for {self.client.name}"

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
