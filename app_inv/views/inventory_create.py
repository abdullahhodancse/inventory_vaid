from django.shortcuts import render,redirect
from app_inv.models.inventory import inventory
from app_inv.forms.inventory_form import InventoryForm
from django.contrib.auth.decorators import login_required
from app_inv.models.user_subscription import UserSubscription
from django.contrib import messages

@login_required
def inventory_create(request):

    try:
       user_subscription=UserSubscription.objects.get(user=request.user)
       user_plan=user_subscription.plan
    except UserSubscription.DoesNotExist:
        messages.error(request,"No active subscription found.")
        return redirect('xpaier')
    
    user_inventory=inventory.objects.filter(user=request.user).count()
    if user_inventory>=user_plan.max_inventory:
       
        return redirect('xpaier')


    if request.method=='POST':
        form=InventoryForm(request.POST,user=request.user)
        if form.is_valid():
            inv=form.save(commit=False)
            inv.user=request.user
            inv.save()
            form.save_m2m()  #for many to many field
            messages.success(request,'Inventory added')
            return redirect('home')
    else:
        form=InventoryForm(user=request.user)
    return render(request,'create_inventory.html',{'form':form})



