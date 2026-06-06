from django.contrib import admin

from .models import Approval


@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):

    list_display = (
        'quotation',
        'approver',
        'status',
        'approved_at'
    )

    list_filter = (
        'status',
    )