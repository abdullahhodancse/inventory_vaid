from django.shortcuts import redirect
from django.urls import reverse
from datetime import date
from app_inv.models.user_subscription import UserSubscription

class SubscriptionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Skip admin panel
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        # Paths that don't require an active subscription
        allowed_paths = [
            reverse('xpaier'),
            reverse('logout'),
            reverse('login'),
            reverse('home'),
        ]

        # Skip check if user is not logged in
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Allow certain URLs without subscription check
        if any(request.path.startswith(path) for path in allowed_paths):
            return self.get_response(request)

        # Check user subscription
        try:
            user_subscription = UserSubscription.objects.get(user=request.user)
        except UserSubscription.DoesNotExist:
            return redirect(reverse('xpaier'))

        # Check if subscription expired
        today = date.today()
        if user_subscription.end_date < today:
            if user_subscription.active:
                user_subscription.active = False
                user_subscription.save()
            return redirect(reverse('xpaier'))

        return self.get_response(request)
