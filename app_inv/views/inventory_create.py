from django.shortcuts import render,redirect
from app_inv.models.inventory import inventory
from app_inv.forms.inventory_form import InventoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def inventory_create(request):
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
        form=InventoryForm()
    return render(request,'create_inventory.html',{'form':form})



