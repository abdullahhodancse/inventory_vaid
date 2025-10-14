from django.db import models
from django.contrib.auth import get_user_model # user for bring custom user model
from app_inv.models.catagory import Catagory

User = get_user_model()

class inventory(models.Model):

    PRIORITY_CHOICES=[
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High')
    ]

    UNIT_CHOICES=[
        ('xxl','extra_extra_large'),
        ('xl','extra_large'),
        ('m','medium'),
        ('s','small'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100,choices=PRIORITY_CHOICES)
    date = models.DateField(auto_now=True)
    catagory = models.ManyToManyField(Catagory,null=True, blank=True)
    current_stock = models.PositiveBigIntegerField(default=10) # it menas the quantity
    minimum_stock=models.PositiveBigIntegerField(default=5,null=True,blank=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='xl',null=True,blank=True)



    def __str__(self):
        return f"{self.name} ({self.priority})"



