from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def verify_email(request, token):
    # token = token.strip().rstrip('/')  # স্পেস ও slash সরানো
    print("Token received:", token)
    
    user = get_object_or_404(User, verification_token__iexact=token)

    if not user.is_active:
        user.is_active = True
        user.is_verified=True
        user.verification_token = None
        user.save()
        messages.success(request, "✅ Email verified successfully! You can now login.")
    else:
        messages.info(request, "Your email is already verified.")

    print("User active status:", user.is_active)
    return redirect("login")


