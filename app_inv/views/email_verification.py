from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def verify_email(request, token):
    print("Token received:", token)
    user = get_object_or_404(User, verification_token=token)

    if not user.is_active:
        user.is_active = True
        user.verification_token = None
        user.save()
        messages.success(request, "✅ Email verified successfully! You can now login.")
    else:
        messages.info(request, "Your email is already verified.")

    print("User active status:", user.is_active)
    return redirect("login")


