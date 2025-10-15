from django.contrib import admin
from app_inv.models.user_subscription import UserSubscription

@admin.register(UserSubscription)
class user__subscription_admin(admin.ModelAdmin):
    list_display=('user','plan','start_date','end_date')
    search_fields=('user',)
    ordering=('start_date',)
    list_filter=('plan',)
    readonly_fields=('start_date','end_date',)


    def has_change_permission(self, request, obj =None):
       if not request.user.is_superuser:
           return False
       return True
    