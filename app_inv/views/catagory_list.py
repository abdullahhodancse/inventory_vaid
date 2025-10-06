from django.shortcuts import render,redirect
from app_inv.models.catagory import Catagory
from django.contrib.auth.decorators import login_required

@login_required
def catagory_list(request):
    cats=Catagory.objects.filter(user=request.user)
    return render(request,'catagory_list.html',{'catagories':cats})



