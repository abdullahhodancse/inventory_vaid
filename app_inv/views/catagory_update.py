from django.shortcuts import render,redirect,get_object_or_404
from app_inv.models.inventory import inventory
from app_inv.models.catagory import Catagory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_inv.forms.catagory_form import catagory



@login_required
def catagory_update_view(request,pk):
    cat=get_object_or_404(Catagory,pk=pk,user=request.user)

    is_used=inventory.objects.filter(catagory=cat).exists()
    if is_used:
        messages.error(request,'cannot update this category — it is used in an inventory.')
        return redirect('catagory_list')
    
    if request.method=='POST':
        form=catagory(request.POST,instance=cat)
        if form.is_valid():
            cat=form.save(commit=False)
            cat.user=request.user
            cat.save()
            messages.success(request,'Category updated successfully!')
            return redirect('catagory_list')
        
    else:
        form=catagory()
    return render(request,'catagory_update.html',{'form':form})

