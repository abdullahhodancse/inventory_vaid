from django.contrib import admin
from app_inv.models.subscription_paln import SubscriptionPlan


@admin.register(SubscriptionPlan)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=('name','duration_days','max_catagoty','max_inventory','price')
    readonly_fields=('duration_days','max_catagoty','max_inventory','price')
    list_filter=('name','price',)
    search_fields=('name','price',)
    ordering=('price',)

    def has_change_permission(self, request, obj =None):
        if not request.user.is_superuser:
            return False
        return True