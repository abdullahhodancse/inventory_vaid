from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_inv.models.inventory import inventory
from django.contrib.auth import get_user_model

User= get_user_model()

@login_required
def profile(request):
    user=request.user
    inventories=inventory.objects.filter(user=user,)
    return render(request, 'profile.html', {'user': user,'inventories':inventories})
