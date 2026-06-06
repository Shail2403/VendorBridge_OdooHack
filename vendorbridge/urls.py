"""
URL configuration for vendorbridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import LoginView, DashboardView


admin.site.site_header = "VendorBridge ERP"
admin.site.site_title = "VendorBridge"
admin.site.index_title = "Procurement Management System"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )