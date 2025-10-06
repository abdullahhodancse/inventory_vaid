from django.contrib import admin
from app_inv.models.inventory import inventory

@admin.register(inventory)
class inventory_admin(admin.ModelAdmin):
    list_display=['id','user','name','priority','date']
    list_filter=['priority','user','date']
    search_fields=['name','property']
    ordering=['priority']









