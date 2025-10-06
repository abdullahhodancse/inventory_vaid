from django.shortcuts import redirect,get_object_or_404
from app_inv.models.catagory import Catagory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError

@login_required
def delete_catagory(request,pk):
    cat=get_object_or_404(Catagory,pk=pk,user=request.user)
    
    try:
        cat.delete()
        messages.success(request,'Catagory deleted')
    except ProtectedError:
        messages.error(request,'Cannot delete this category — it is used in an inventory.')
        return redirect('catagory_list')
    return redirect('catagory_list')


