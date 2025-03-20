from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),         # Custom signup and logout routes
    path("accounts/", include("django.contrib.auth.urls")),  # Login, password reset, etc.
    path("", include("pages.urls")),           
    path("workorders/", include("workorders.urls")),  # Work Orders routes
    path("clients/", include("clients.urls")),
    path("invoices/", include("invoices.urls")),
    path("workorders/", include("workorders.urls")),
    path("invoices/", include("invoices.urls")),


             # Home and other pages
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
