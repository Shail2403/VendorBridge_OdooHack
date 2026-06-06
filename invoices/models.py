from django.db import models

from procurement.models import Quotation


class PurchaseOrder(models.Model):

    po_number = models.CharField(
        max_length=50,
        unique=True
    )

    quotation = models.OneToOneField(
        Quotation,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.po_number
    
class Invoice(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
    )

    invoice_number = models.CharField(
        max_length=50,
        unique=True
    )

    purchase_order = models.OneToOneField(
        PurchaseOrder,
        on_delete=models.CASCADE
    )

    tax_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18.00
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    pdf_file = models.FileField(
        upload_to='invoices/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.invoice_number
    
class ActivityLog(models.Model):

    user = models.CharField(
        max_length=255
    )

    action = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.action