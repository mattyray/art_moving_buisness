from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("pages.urls")),           
    path("workorders/", include("workorders.urls")),
    path("clients/", include("clients.urls")),
    path("invoices/", include("invoices.urls")),
    path('calendar/', include('calendar_app.urls', namespace='calendar_app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # ✅ ADD THIS LINE - this is what's missing!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    