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

    def save(self,*args,**kwargs):
        if self.name=='Free':
            self.duration_days=3
            self.max_catagoty=3
            self.max_inventory=3
            self.price=0.00
        
        elif self.name=='Pro':
            self.duration_days=30
            self.max_catagoty=50
            self.max_inventory=50
            self.price=399.00

        elif self.name=='Gold':
            self.duration_days=30
            self.max_catagoty=100
            self.max_inventory=100
            self.price=599.00
        super().save(*args,**kwargs) # feild e jodi extara logic diya ba customize data set korte cai tokhon aita lage,,mane databse save korar age data change korle,,,,,
    
    def __str__(self):
        return f"{self.name}"