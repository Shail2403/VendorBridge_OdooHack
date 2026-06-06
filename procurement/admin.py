from django.contrib import admin

from .models import RFQ, Quotation


@admin.register(RFQ)
class RFQAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'quantity',
        'deadline',
        'status',
        'created_by'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'title',
    )


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):

    list_display = (
        'vendor',
        'rfq',
        'price',
        'delivery_days',
        'status'
    )

    list_filter = (
        'status',
    )