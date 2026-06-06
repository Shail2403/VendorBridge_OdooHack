from django.conf import settings
from django.db import models

from vendors.models import Vendor


class RFQ(models.Model):

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('APPROVED', 'Approved'),
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    quantity = models.PositiveIntegerField()

    attachment = models.FileField(
        upload_to='rfq_attachments/',
        blank=True,
        null=True
    )

    deadline = models.DateField()

    vendors = models.ManyToManyField(
        Vendor,
        related_name='rfqs'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Quotation(models.Model):

    STATUS_CHOICES = (
        ('SUBMITTED', 'Submitted'),
        ('SELECTED', 'Selected'),
        ('REJECTED', 'Rejected'),
    )

    rfq = models.ForeignKey(
        RFQ,
        on_delete=models.CASCADE
    )

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    delivery_days = models.PositiveIntegerField()

    notes = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SUBMITTED'
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.vendor} - {self.rfq}"