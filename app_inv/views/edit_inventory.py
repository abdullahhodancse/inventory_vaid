from django.shortcuts import redirect,render,get_object_or_404
from app_inv.models import inventory
from app_inv.forms.inventory_form import  InventoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def edit_inventory(request,pk):
    inv=get_object_or_404(inventory,id=pk)
    if request.method=='POST':
        form=InventoryForm(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'inventory updated')
            return redirect('home')
    else:
        form=InventoryForm(instance=inv)
    return render(request,'inv_edit.html',{'form':form})


        



