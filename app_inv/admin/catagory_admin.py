from django.contrib import admin
from app_inv.models.catagory import Catagory

@admin.register(Catagory)
class catagory_admin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
    list_filter=['name']
    ordering=['name']
