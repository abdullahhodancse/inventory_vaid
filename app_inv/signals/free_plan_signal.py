from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from app_inv.models.subscription_paln import SubscriptionPlan
from app_inv.models.user_subscription  import UserSubscription
from datetime import date,timedelta

User=get_user_model()

@receiver(post_save,sender=User)
def assign_free_plan(sender,instance,created,**kwargs):
    if created:
        try:
            free_plan=SubscriptionPlan.objects.get(name="Free")
            UserSubscription.objects.create(
                user=instance,
                plan=free_plan,
                start_date=date.today(),
                end_date=date.today()+timedelta(days=free_plan.duration_days)
            )
        except SubscriptionPlan.DoesNotExist:
            pass
        