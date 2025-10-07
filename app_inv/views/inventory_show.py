from django.shortcuts import render,redirect
from app_inv.models.inventory import inventory


def Show_inventory(request):
    inventories=inventory.objects.all()
    return render(request,'home.html',{'inventories':inventories})