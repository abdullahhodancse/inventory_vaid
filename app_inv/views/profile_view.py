from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_inv.models.inventory import inventory
from django.contrib.auth import get_user_model
from app_inv.views.subscription_view import create_subscription
from app_inv.models.user_subscription import UserSubscription

User= get_user_model()

@login_required
def profile(request):
    user=request.user
    inventories=inventory.objects.filter(user=user)

    try:
        user_subscription=UserSubscription.objects.get(user=user)
    except UserSubscription.DoesNotExist:
        user_subscription=None
    return render(request, 'profile.html', {'user': user,'inventories':inventories, 'user_subscription':user_subscription})
