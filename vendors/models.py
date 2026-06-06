from django.db import models


class Vendor(models.Model):

    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )

    company_name = models.CharField(
        max_length=255
    )

    gst_number = models.CharField(
        max_length=30,
        unique=True
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15
    )

    address = models.TextField()

    category = models.CharField(
        max_length=100
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.company_name