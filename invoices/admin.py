from django.contrib import admin

from .models import (
    PurchaseOrder,
    Invoice,
    ActivityLog
)


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):

    list_display = (
        'po_number',
        'quotation',
        'amount',
        'created_at'
    )


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):

    list_display = (
        'invoice_number',
        'purchase_order',
        'total_amount',
        'status'
    )

    list_filter = (
        'status',
    )


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'action',
        'created_at'
    )