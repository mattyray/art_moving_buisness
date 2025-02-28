from django.contrib import admin
from django.urls import path, include
from accounts.views import custom_logout  # Ensure custom_logout is imported

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/logout/", custom_logout, name="logout"),  # Uses custom logout function
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),

    path("", include("pages.urls")),  # Ensure home route exists
]
