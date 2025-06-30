from django.urls import path
from .views import custom_logout

urlpatterns = [
    # path("signup/", SignupPageView.as_view(), name="signup"),  # Removed - admin only user creation
    path("logout/", custom_logout, name="logout"),
]