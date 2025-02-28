from django.urls import path
from .views import SignupPageView, custom_logout

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("logout/", custom_logout, name="logout"),  # Ensure this is correct
]
