from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    """Logs out the user and redirects to the homepage."""
    print("🚀 custom_logout was called!")
    request.session.flush()  # Clears session data manually
    logout(request)
    return redirect("/")  # Redirect to the root URL explicitly

# SignupPageView removed - users created through admin only