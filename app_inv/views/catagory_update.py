from django.shortcuts import render,redirect,get_object_or_404
from app_inv.models.inventory import inventory
from app_inv.models.catagory import Catagory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_inv.forms.catagory_form import catagory



@login_required
def catagory_update_view(request,pk):
    cat=get_object_or_404(Catagory,pk=pk,user=request.user)

    is_used=inventory.objects.filter(catagory=cat).exists() # check catagory is used in inventory or not
    if is_used:
        messages.error(request,'cannot update this category — it is used in an inventory.')
        return redirect('catagory_list')
    
    if request.method=='POST':
        form=catagory(request.POST)
        if form.is_valid():
            cat=form.save(commit=False) #form  er data theke ekta object create and not save in db
            cat.user=request.user #obect e curent login user add kora
            cat.save()
            messages.success(request,'Category updated successfully!')
            return redirect('catagory_list')
        
    else:
        form=catagory(instance=cat)  #isintance er maddhome ager data gula show kora jai
    return render(request,'catagory_update.html',{'form':form}) #template e from pathano holo

