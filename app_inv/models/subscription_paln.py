from django.db import models

class SubscriptionPlan(models.Model):
    PLAN_CHOICES=[
        ('Free','Free'),
        ('Pro','Pro'),
        ('Gold','Gold'),

    ]
    name=models.CharField(max_length=50,unique=True,choices=PLAN_CHOICES)
    duration_days=models.PositiveBigIntegerField(default=0)
    max_catagoty=models.PositiveBigIntegerField(default=0)
    max_inventory=models.PositiveBigIntegerField(default=0)
    price=models.DecimalField(max_digits=6,decimal_places=2,default=0.00)

    
    
    def __str__(self):
        return f"{self.name}"