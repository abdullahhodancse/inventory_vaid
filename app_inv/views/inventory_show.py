from django.shortcuts import render,redirect
from app_inv.models.inventory import inventory






from django.shortcuts import render, redirect
from app_inv.models.user_subscription import UserSubscription

def Show_inventory(request):
    if not request.user.is_authenticated:
        # redirect to login page if user is not logged in
        return redirect('login')  # replace 'login' with your login URL name

    # user is authenticated, safe to query
    try:
        user_subscription = UserSubscription.objects.get(user=request.user)
    except UserSubscription.DoesNotExist:
        user_subscription = None  # or handle this case as you want

    # Your inventory logic here
    inventories = inventory.objects.all()
    urgent_items = []
    normal_items = []

    for item in inventories:
        if item.current_stock > item.minimum_stock:
            normal_items.append(item)
        else:
            urgent_items.append(item)

    context = {
        'urgent_items': urgent_items,
        'normal_items': normal_items,
        'user_subscription': user_subscription,
    }

    return render(request, 'home.html', context)
