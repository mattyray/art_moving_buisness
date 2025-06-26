from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    billing_address = models.CharField(max_length=255, blank=True, null=True)  # ✅ NEW FIELD

    def __str__(self):
        return self.name