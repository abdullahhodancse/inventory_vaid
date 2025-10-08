from django.shortcuts import redirect,get_object_or_404
from app_inv.models.catagory import Catagory
from app_inv.models.inventory import inventory
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def delete_catagory(request,pk):
    cat=get_object_or_404(Catagory,pk=pk,user=request.user)
    is_used=inventory.objects.filter(catagory=cat).exists()
    if  is_used:
        messages.error(request,'cannot delete this category — it is used in an inventory.')
        return redirect('catagory_list')
    else:
        cat.delete()
        messages.success(request,'Catagory deleted')
        
    return redirect('catagory_list')
    
    

