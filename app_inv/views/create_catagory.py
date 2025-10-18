from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from app_inv.forms.catagory_form import Catagory_form
from app_inv.models.catagory import Catagory
from app_inv.models.user_subscription import UserSubscription

from django.contrib import messages


@login_required



def add_catagory(request):

    try:
        user_subscription=UserSubscription.objects.get(user=request.user)
        user_plan=user_subscription.plan
    except UserSubscription.DoesNotExist:
        messages.error(request,'No subscription found. Please contact support.')
    
    catagory_count=Catagory.objects.filter(user=request.user).count()
    if catagory_count>=user_plan.max_catagoty:
        messages.error(request,"your catagory limit has been full filled")
        return redirect('catagory_list')

    if request.method=='POST':
        form=Catagory_form(request.POST)
        if form.is_valid():
            cat=form.save(commit=False)
            cat.user=request.user
            cat.save()
            messages.success(request,'catagory added')
            return redirect('catagory_list')
        
    else:
        form=Catagory_form()
    return render(request,'add_catagory.html',{'form':form})    
