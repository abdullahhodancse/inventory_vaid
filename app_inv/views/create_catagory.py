from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from app_inv.forms.catagory_form import catagory

from django.contrib import messages


@login_required
def add_catagory(request):
    if request.method=='POST':
        form=catagory(request.POST)
        if form.is_valid():
            cat=form.save(commit=False)
            cat.user=request.user
            cat.save()
            messages.success(request,'catagory added')
            return redirect('catagory_list')
        
    else:
        form=catagory()
    return render(request,'add_catagory.html',{'form':form})    
