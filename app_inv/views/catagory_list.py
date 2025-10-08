from django.shortcuts import render
from app_inv.models.catagory import Catagory
from django.contrib.auth.decorators import login_required

@login_required
def catagory_list(request):
    cats=Catagory.objects.filter(user=request.user) #show inly login user catagory
    return render(request,'catagory_list.html',{'catagories':cats})



