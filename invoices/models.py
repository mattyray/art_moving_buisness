import random
from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Not in QuickBooks'),
        ('in_quickbooks', 'In QuickBooks'),
        ('paid', 'Paid'),
    ]

    
    invoice_number = models.CharField(max_length=50, unique=True, blank=True)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='invoices')
    # Optional: link to a work order
    work_order = models.ForeignKey(
        'workorders.WorkOrder',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='invoices'
    )
    date_created = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpaid')
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = ""  # Set empty first
        super().save(*args, **kwargs)
        if not self.invoice_number:  # After save, we have an ID
            self.invoice_number = str(self.id)
            super().save(update_fields=['invoice_number'])

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client.name}"