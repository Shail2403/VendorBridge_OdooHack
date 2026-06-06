from django.contrib import admin

from .models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

    list_display = (
        'company_name',
        'category',
        'email',
        'rating',
        'status'
    )

    search_fields = (
        'company_name',
        'gst_number'
    )

    list_filter = (
        'status',
        'category'
    )