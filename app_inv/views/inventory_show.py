from django.shortcuts import render,redirect
from app_inv.models.inventory import inventory


def Show_inventory(request):
    inventories=inventory.objects.all()
    urgent_items=[]
    normal_items=[]
    for item in inventories:
        if item.current_stock>item.minimum_stock:
            normal_items.append(item)
        else:
            urgent_items.append(item)
    context={
        'urgent_items':urgent_items,
        'normal_items': normal_items,
    }        
    return render(request,'home.html',context)