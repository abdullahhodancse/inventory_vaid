from django.db import models
from django.contrib.auth import get_user_model
from app_inv.models.subscription_paln import SubscriptionPlan
from datetime import timedelta,date

User=get_user_model()

class UserSubscription(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    plan=models.ForeignKey(SubscriptionPlan,on_delete=models.DO_NOTHING,null=True)
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.end_date and self.plan:
            self.end_date= date.today()+timedelta(self.plan.duration_days)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.user.email}-{self.plan.name}" 

