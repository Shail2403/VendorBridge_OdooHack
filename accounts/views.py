from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from vendors.models import Vendor
from procurement.models import RFQ
from approvals.models import Approval
from invoices.models import Invoice


class LoginView(DjangoLoginView):
    template_name = "login.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["vendors_count"] = Vendor.objects.count()
        context["rfq_count"] = RFQ.objects.count()
        context["approval_count"] = Approval.objects.count()
        context["invoice_count"] = Invoice.objects.count()

        return context