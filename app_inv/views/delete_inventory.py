from django.shortcuts import redirect,get_object_or_404
from app_inv.models import inventory
from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required
def delete_inventory(requst,pk):
    inv=get_object_or_404(inventory,id=pk,user=requst.user)
    inv.delete()
    messages.success(requst,'Inventory deletes successfully')
    return redirect('profile')

    